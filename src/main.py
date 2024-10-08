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
        JSON: status_code = 200, информация о выполнении функции
    """
    if pgsql.create_all_tables():
        return {'message:', 'Таблицы созданы!'}
    raise HTTPException(501, 'Сервер не обработал запрос')


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
