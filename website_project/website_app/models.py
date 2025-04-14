from django.db import models
from django.urls import reverse


# Класс представления таблицы в БД для хранения информации о командах
class Command(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        ordering = ('pk',)


# Класс представления таблицы в БД для хранения информации о группах команд
class Group(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title


# Класс представления таблицы в БД для хранения информации о направления компании
class About(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True)
