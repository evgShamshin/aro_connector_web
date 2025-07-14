# Скрипт для добавления записей в БД в models
import os
import django
import sys
from django.core.files import File
from pathlib import Path
from django.conf import settings

# Добавляем корень проекта в PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Указываем Django, где настройки
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aro_web.settings")  # Укажи правильное имя проекта

# Инициализируем Django
django.setup()

# Теперь можно импортировать модели и работать с ними
from aro_app.models import WebsiteApp

file_path_media = Path(settings.MEDIA_ROOT)

with open(file_path_media / "ViewExceptionKeys_32.svg") as img:
    WebsiteApp.objects.filter(title__icontains="Ключи исключения").update(image=File(img))
    print(f"Запись {img.__class__} обновлена")

with open(file_path_media / "CherryPicker_32.svg") as img:
    WebsiteApp.objects.filter(title__icontains="Суперфильтр").update(image=File(img))
    print(f"Запись {img.__class__} обновлена")

with open(file_path_media / "ElementIndexer_32.svg") as img:
    WebsiteApp.objects.filter(title__icontains="Маркировка элементов").update(image=File(img))
    print(f"Запись {img.__class__} обновлена")
