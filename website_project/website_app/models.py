from django.db import models


class WebsiteApp(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    article_slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='media/', blank=True)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True, blank=True)
    # time_create = models.DateTimeField(auto_now_add=True)
    # time_update = models.DateTimeField(auto_now=True)
    # is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ('pk',)


class Group(models.Model):
    title = models.CharField(max_length=255)
    article_slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

