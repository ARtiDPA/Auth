"""Точка входа системы."""
from fastapi import FastAPI

from routes.system.route import app as route_three
from routes.tokens.route import app as route_two
from routes.user.route import app as route

app = FastAPI()

app.include_router(router=route, tags=['User'])
app.include_router(router=route_two, tags=['Tokens'])
app.include_router(router=route_three, tags=['System'])
