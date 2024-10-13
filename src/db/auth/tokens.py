"""Файл по работе с JWT токенами."""
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Union

JWT_SEKRET_KEY = 'ABOBA'
ALGORITM = 'HS256'


class Tokens():
    def __init__(self):
        pass

    def create_access_tokens(self, id: int) -> str:
        expires = datetime.now() + timedelta(minutes=15) 
        jwt_decode = {'exp': expires, 'sub': str(id)}
        return jwt.encode(jwt_decode, JWT_SEKRET_KEY, ALGORITM)


    def create_refresh_tokens(self, id: int) -> str:
        expires = datetime.now() + timedelta(days=7)
        jwt_decode = {'exp': expires, 'sub': str(id)}
        return jwt.encode(jwt_decode, JWT_SEKRET_KEY, ALGORITM)
    

    def verifi_tokens(self, access_tokens: str) -> Union[str, bool]:
        try:
            return jwt.decode(access_tokens, JWT_SEKRET_KEY, ALGORITM)
        except JWTError:
            return False


tokens = Tokens()
