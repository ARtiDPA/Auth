"""Файл маршрутизаторов токенов."""
from fastapi import APIRouter, HTTPException

from db.auth.tokens import tokens

app = APIRouter(prefix='/tokens')


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