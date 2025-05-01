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

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    slug = models.SlugField(blank=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True, blank=True)
    tag = models.ManyToManyField('Tag', blank=True)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Команды"
        verbose_name_plural = "Команды"
        ordering = ('pk',)

    def get_absolute_url(self):
        return reverse('connector_commands', kwargs={'article_slug': self.slug})


# Информация о группах команд
class Group(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title


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
