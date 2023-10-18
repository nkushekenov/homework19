import os
import django
import random

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homework19.settings')
django.setup()

# Импортирование модели пользователя
from HW19.models import User

def add_user(username, email):
    # Создание нового экземпляра пользователя
    user = User(username=username, email=email)
    user.save()  # Сохранение пользователя в базе данных

def populate_users():
    # Добавление 10 пользователей
    for i in range(10):
        username = f"user_{i}"
        email = f"user_{i}@example.com"
        add_user(username, email)

# Выполнение скрипта
if __name__ == "__main__":
    populate_users()
