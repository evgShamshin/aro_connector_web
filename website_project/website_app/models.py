from django.db import models


class WebsiteApp(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    article_slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='media/', blank=True)
    # time_create = models.DateTimeField(auto_now_add=True)
    # time_update = models.DateTimeField(auto_now=True)
    # is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)


class About(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True)