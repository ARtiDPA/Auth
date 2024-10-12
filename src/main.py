"""Точка входа системы."""
from fastapi import FastAPI
from db.db import pgsql
import uvicorn
from fastapi import HTTPException


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

    Returns:
        JSON: status_code
    """
    if password == two_password:
        if pgsql.found_user(login):
            pgsql.create_acaunt(login, password)
            return {'message', 'акаунт создан'}
        return HTTPException(409, 'error: акаунт с таким именем уже создан')
    return HTTPException(412, 'error: пароли не совпадают')


@app.post('/authorization')
def authorrization(login: str,
                   password: str
                   ):
    if pgsql.found_user(login):
        return {'message': 'all rigth user is found)'}
    return HTTPException(404, 'error: пользователь с таким имене отсуствует')        

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
