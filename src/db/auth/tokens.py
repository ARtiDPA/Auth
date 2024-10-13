"""Файл по работе с JWT токенами."""
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Union

JWT_SEKRET_KEY = 'ABOBA'
ALGORITM = 'HS256'


class JwtTokens():
    """Класс по работе с JWT токенами."""

    def __init__(self):
        """Init file."""
        pass

    def create_access_tokens(self, id_user: int) -> str:
        """Создайние access токена.

        Args:
            id_user (int): айди пользователя

        Returns:
            str: access токен
        """
        expires = datetime.now() + timedelta(minutes=15) 
        jwt_decode = {'exp': expires, 'sub': str(id)}
        return jwt.encode(jwt_decode, JWT_SEKRET_KEY, ALGORITM)

    def create_refresh_tokens(self, id_user: int) -> str:
        """Создание refresh токена.

        Args:
            id_user (int): айди пользователя

        Returns:
            str: refresh токен
        """
        expires = datetime.now() + timedelta(days=7)
        jwt_decode = {'exp': expires, 'sub': str(id)}
        return jwt.encode(jwt_decode, JWT_SEKRET_KEY, ALGORITM)

    def verifi_tokens(self, access_tokens: str) -> Union[str, bool]:
        """Проверка токена.

        Args:
            access_tokens (str): access токен

        Returns:
            Union[str, bool]: [payload, Ошибка декдирование токена]
        """
        try:
            return jwt.decode(access_tokens, JWT_SEKRET_KEY, ALGORITM)
        except JWTError:
            return False


tokens = JwtTokens()
