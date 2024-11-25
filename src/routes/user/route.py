"""Маршрутизаторы пользователя."""
from fastapi import APIRouter, HTTPException

from db.auth.hash import hashed
from db.auth.tokens import tokens
from db.db import pgsql, redis

app = APIRouter(prefix='/user')


@app.post('/register')
def register(
    login: str,
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
def authorrization(
    login: str,
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
            access_token = redis.get_key(str(user.id) + '_' + 'access_token')
            refresh_token = redis.get_key(str(user.id) + '_' + 'refresh_token')
            if access_token:
                return {
                    'access token: ': access_token,
                    'refresh tokne: ': refresh_token,
                }
            elif refresh_token:
                redis.delete_key(user.id + '_' + 'refresh_token')

            access_token = tokens.create_access_tokens(user.id)
            refresh_token = tokens.create_refresh_tokens(user.id)
            redis.set_key(str(user.id) + '_' + 'access_token', access_token, 15 * 60)
            redis.set_key(str(user.id) + '_' + 'refresh_token', refresh_token, 7 * 24 * 60 * 60)
            return {
                'access token: ': access_token,
                'refresh tokne: ': refresh_token,
            }
        raise HTTPException(403, 'eror: пароли не совпадают')
    raise HTTPException(404, 'error: пользователь с таким имене отсутствует')