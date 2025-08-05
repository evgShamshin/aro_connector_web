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
    slug = models.SlugField(max_length=255, blank=True, verbose_name='Slug')
    gif = models.ImageField(max_length=255, upload_to='media/aro_app/gif', verbose_name='GIF-Изображение',
                            blank=True, null=True)
    confluence_link = models.URLField(blank=True, null=True, verbose_name='Confluence')
    rutube_link = models.URLField(blank=True, null=True, verbose_name='Rutube')
    vkontakte_link = models.URLField(blank=True, null=True, verbose_name='Вконтакте')
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Стоимость')
    is_published = models.IntegerField(choices=Status.choices, default=Status.DRAFT, verbose_name='Статус')
    image = models.ImageField(max_length=255, upload_to='media/aro_app/image', blank=True, null=True,
                              verbose_name='Изображение')
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Группа")
    tag = models.ManyToManyField('Tag', blank=True, verbose_name='Тэг')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        ordering = ('group', 'pk')

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
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)


class Consult(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    attachment = models.FileField(upload_to='aro_app/attachment', blank=True)
