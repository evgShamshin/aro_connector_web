from django.contrib.sitemaps import Sitemap
from .models import Command


class PostSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Command.objects.all()
