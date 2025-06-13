from django import template
from django.db.models import Count

from website_app.models import Group, Tag

register = template.Library()


@register.inclusion_tag('website_app/groups.html')
def show_groups(cat_selected=0):
    groups = Group.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {'groups': groups, 'cat_selected': cat_selected}

# @register.inclusion_tag('women/list_tags.html')
# def show_all_tags():
#     return {'tags': TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)}
