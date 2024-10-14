"""Точка входа системы."""
import json

import uvicorn
from fastapi import FastAPI, HTTPException

from db.auth.hash import hashed
from db.auth.tokens import tokens
from db.db import pgsql

app = FastAPI()


@app.get('/startup')
def statup():
    """Маршрутизатор создаяния таблиц в бд.

    Raises:
        HTTPException: ошибка о проблемах на сервере.

    Returns:
        JSON: status_code
    """
    if pgsql.create_all_tables():
        return {'message:', 'Таблицы созданы!'}
    raise HTTPException(501, 'Сервер не обработал запрос')


@app.post('/register')
def register(login: str,
             password: str,
             two_password: str,
             ):
    """Маршрутизатор регистрации.

    Args:
        login (str): логин пользователя
        password (str): пароль
        two_password (str): второй пароль

    Raises:
        HTTPException: Пользователь с таким именем уже сущетсвует
        HTTPException: Пароли не совпадают

    Returns:
        _type_: _description_
    """
    if password == two_password:
        if not pgsql.found_user(login):
            pgsql.create_acaunt(login, password)
            return {'message', 'акаунт создан'}
        raise HTTPException(409, 'error: акаунт с таким именем уже создан')
    raise HTTPException(412, 'error: пароли не совпадают')


@app.post('/authorization')
def authorrization(login: str,
                   password: str,
                   ):
    """Маршрутизатор авторизации.

    Args:
        login (str): логин пользователя
        password (str): пароль пользователя

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    if pgsql.found_user(login):
        user = pgsql.get_user(login)
        if hashed.check_password(
            hash_password=user.password,
            password=password,
        ):
            return {
                'access token: ': tokens.create_access_tokens(user.id),
                'refresh tokne: ': tokens.create_refresh_tokens(user.id),
            }
        return HTTPException(403, 'eror: пароли не совпадают')
    raise HTTPException(404, 'error: пользователь с таким имене отсутствует')


@app.post('/valid_tokens')
def valid_tokens(access_token: str):
    """Маршрутизатор проверки токена.

    Args:
        access_token (str): access_token

    Raises:
        HTTPException: ошибка токена

    Returns:
        JSON: данные о пользователе
    """
    result = tokens.verifi_tokens(access_token)
    if result:
        return {
            'message': 'токен действителен',
            'user_id': result,
            }
    raise HTTPException(401, 'токен не действителен')


@app.post('/update_tokens')
def update_tones(refresh_tokens: str):
    """Маршрутизатор обновление токенов.

    Args:
        refresh_tokens (str): refresh токен

    Raises:
        HTTPException: Ошибка при валидации токена

    Returns:
        json: access и refresh токены
    """
    payload = tokens.verifi_tokens(refresh_tokens)
    if payload:
        user_id = payload.get('sub')
        access_token = tokens.create_access_tokens(user_id)
        refresh_tokens = tokens.create_refresh_tokens(user_id)
        return {
            'access_token': access_token,
            'refresh_token': refresh_tokens,
        }
    raise HTTPException(401, 'error: токен не действителен')
     

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
