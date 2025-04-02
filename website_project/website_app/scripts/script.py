# Скрипт для добавления записей в БД в models
import os
import django
import sys

# Добавляем корень проекта в PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Указываем Django, где настройки
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website_project.settings")  # Укажи правильное имя проекта

# Инициализируем Django
django.setup()

# Теперь можно импортировать модели и работать с ними
from website_app.models import WebsiteApp

print(WebsiteApp.objects.get(pk=1))