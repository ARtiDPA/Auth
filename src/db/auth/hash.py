"""Файл для работы с хэшем."""
import bcrypt


class Hashed:
    """Класс для работы с хэшем."""

    def __init__(self):
        """Init func."""
        self.salt = bcrypt.gensalt()

    def create_hash(self, password: str) -> bytes:
        """Хэширование пароля.

        Args:
            password (str): пароль пользователя

        Returns:
            bytes: хэшированный пароль
        """
        return bcrypt.hashpw(password.encode('utf-8'), self.salt).decode(
            'utf-8',
        )

    def check_password(self, hash_password: str, password: str) -> bool:
        """Проверка паролей.

        Args:
            hash_password (str): Хэшированный пароль
            password (str): пароль

        Returns:
            bool: True если совпадают пароли иначе False
        """
        return bcrypt.checkpw(
            password.encode('utf-8'), 
            hash_password.encode('utf-8'),
            )


hashed = Hashed()
