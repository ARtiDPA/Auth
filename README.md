# Микросервис авторизации/регистрации на FastAPI
---
## Инструкция по запуску:
ВНИМАНИЕ! Перед запуском у вас должен быть установлен Docker

1. [Docker](https://docker.qubitpi.org/desktop/setup/install/windows-install/) для скачивания

2. клонируем репозиторий `git clone https://github.com/ARtiDPA/Auth`

3. переходим в проект `cd Auth`
   
4. Изменям название файла с `.env.example` на `.env`

5. Далее выполнить команду: `docker compose up --build`
---
## Скриншоты запущенного приложение:
- ![image](https://github.com/user-attachments/assets/6ecbdb0b-4cbb-4360-8754-3894c64b7bff)
  
- ![image](https://github.com/user-attachments/assets/b2439bad-8f3c-4088-b69d-edfe6d2337df)

- ![image](https://github.com/user-attachments/assets/ed193fa2-7246-4ea1-9f28-21f38c314080)

- ![image](https://github.com/user-attachments/assets/f1848dc5-d3dd-4f80-9c21-54a956e89abe)

- ![image](https://github.com/user-attachments/assets/a7b20db4-96b6-4bc9-8976-728fdfc910f7)
---
## архетиктура файлов сервиса
```
Auth:
│   main.py - Точка входа
│   __init__.py
│   
├───db
│   │   config.py - файл настроек
│   │   db.py - файл для работы с БД
│   │   models.py - Модели для БД
│   │   __init__.py
│   │   
│   └───auth
│           hash.py - файл для работы с хэш
│           tokens.py - файл для работы с JWT-токенами
│           __init__.py       
│
└───routes - маршрутизаторы 
    ├───system
    │      route.py
    │      __init__.py
    │ 
    │   
    │
    ├───tokens
    │      route.py
    │      __init__.py
    │  
    └───user
        │   route.py
        │   __init__.py

```

---
## Технологии:
- FastAPI
- PostgreSQL
- Redis
- sqlalchemy
- JWT
- Uvicorn
- Docker
- DocString
---
## Разработчики:
- Артём Данилов
