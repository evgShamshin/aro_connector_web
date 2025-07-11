from django import template

from aro_app.models import Group, Tag, About

register = template.Library()


@register.simple_tag()
def show_groups():
    groups = Group.objects.all()
    return groups


@register.simple_tag()
def show_tags():
    tags = Tag.objects.all()
    return tags


@register.simple_tag()
def show_abouts():
    abouts = About.objects.all()
    return abouts
