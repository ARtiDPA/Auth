"""Файл по работе с JWT токенами."""
from datetime import datetime, timedelta
from typing import Union

from jose import JWTError, jwt

from ..config import jwtsettings


class JwtTokens():
    """Класс по работе с JWT токенами."""

    def __init__(self):
        """Init file."""
        self.algoritm = jwtsettings.ALGORITHM
        self.jwt_sekret_key = jwtsettings.JWT_SEKRET_KEY
        self.time_access = jwtsettings.ACCESS_TIME
        self.time_refresh = jwtsettings.REFRESH_TIME

    def create_access_tokens(self, id_user: int) -> str:
        """Создайние access токена.

        Args:
            id_user (int): айди пользователя

        Returns:
            str: access токен
        """
        expires = datetime.now() + timedelta(minutes=self.time_access) 
        jwt_decode = {'exp': expires, 'sub': str(id_user)}
        return jwt.encode(jwt_decode, self.jwt_sekret_key, self.algoritm)

    def create_refresh_tokens(self, id_user: int) -> str:
        """Создание refresh токена.

        Args:
            id_user (int): айди пользователя

        Returns:
            str: refresh токен
        """
        expires = datetime.now() + timedelta(days=self.time_refresh)
        jwt_decode = {'exp': expires, 'sub': str(id_user)}
        return jwt.encode(jwt_decode, self.jwt_sekret_key, self.algoritm)

    def verifi_tokens(self, access_tokens: str) -> Union[str, bool]:
        """Проверка токена.

        Args:
            access_tokens (str): access токен

        Returns:
            Union[str, bool]: [payload, Ошибка декдирование токена]
        """
        try:
            return jwt.decode(
                access_tokens,
                self.jwt_sekret_key,
                self.algoritm,
            )
        except JWTError:
            return False


tokens = JwtTokens()
