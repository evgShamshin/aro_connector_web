from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .models import Command, About, Group, Tag


# Главная страница сайта
def connector_page(request: HttpRequest):  # HttpResponse
    data = {'title': 'Набор команд',
            'about': About.objects.all(),
            'commands': Command.objects.select_related('group').prefetch_related(
                Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')).filter(is_published=1),
            'tags': Tag.objects.all(),
            'groups': Group.objects.all()}

    return render(request, 'website_app/main.html', context=data)


# Главная страница с фильтрацией по категориям
def connector_page_by_group(request: HttpRequest, group_slug) -> HttpResponse:
    data = {'title': 'Набор команд',
            'title_group': Group.objects.filter(slug=group_slug).get(),
            'about': About.objects.all(),
            'groups': Group.objects.all(),
            'tags': Tag.objects.all(),
            'commands': Command.objects.filter(group=get_object_or_404(Group, slug=group_slug))
            .select_related('group').prefetch_related(
                Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')).filter(is_published=1), }

    return render(request, 'website_app/main.html', context=data)


# Главная страница с фильтрацией по тегам
def connector_page_by_tag(request: HttpRequest, tag_slug) -> HttpResponse:
    tag = get_object_or_404(Tag, slug=tag_slug)

    data = {'title': 'Набор команд',
            'title_tag': Tag.objects.filter(slug=tag_slug).get(),
            'about': About.objects.all(),
            'groups': Group.objects.all(),
            'tags': Tag.objects.all(),
            'tag': get_object_or_404(Tag, slug=tag_slug),
            'commands': Command.objects.filter(tag=tag)  # Фильтруем команды по тегу
            .select_related('group')  # Оптимизация для ForeignKey
            .prefetch_related(
                Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')
            ).filter(is_published=1), }

    return render(request, 'website_app/main.html', context=data)


# Страница команды
def connector_commands_page(request: HttpRequest, article_slug) -> HttpResponse:
    data = {'title': 'Команда',
            'about': About.objects.all(),
            'groups': Group.objects.all(),
            'tags': Tag.objects.all(),
            'obj': get_object_or_404(Command, slug=article_slug), }

    return render(request, 'website_app/command.html', context=data)


# Страница в случае отсутствия результата
def nof_found_page(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')
