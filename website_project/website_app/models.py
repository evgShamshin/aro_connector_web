from django.db import models
from django.urls import reverse


# Информация об опубликованных командах
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Command.Status.PUBLISHED)


# Информация о командах
class Command(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'В разработке'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Команда')
    description = models.TextField(blank=True, verbose_name='Описание')
    link = models.URLField(blank=True, verbose_name='Документация')
    slug = models.SlugField(blank=True, verbose_name='Slug')
    is_published = models.IntegerField(choices=Status.choices, default=Status.DRAFT, verbose_name='Статус')
    image = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name='Изображение')
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True, blank=True,verbose_name="Группа")
    tag = models.ManyToManyField('Tag', blank=True, verbose_name='Тэг')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        ordering = ('pk',)

    def get_absolute_url(self):
        return reverse('connector_commands', kwargs={'article_slug': self.slug})


# Информация о группах команд
class Group(models.Model):
    title = models.CharField(max_length=255, verbose_name="Группа")
    slug = models.SlugField(blank=True, verbose_name="Slug")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ('pk',)


# Информация о тегах команд
class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title


# Информации о направлениях компании
class About(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True)


class User(models.Model):
    slug = models.SlugField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)