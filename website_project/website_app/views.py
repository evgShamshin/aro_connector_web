from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .models import Command, About, Group

about = About.objects.all()
data = {'title': 'Набор команд',
        'about': about,
        'commands': Command.objects.all(),
        'groups': Group.objects.all()}


# Главная страница сайта
def connector_page(request: HttpRequest):  # HttpResponse
    return render(request, 'website_app/main.html', context=data)


# Главная страница с фильтрацией по категориям
def connector_page_by_group(request: HttpRequest, group_slug) -> HttpResponse:
    group = get_object_or_404(Group, slug=group_slug)
    data['commands'] = Command.objects.filter(group=group)

    return render(request, 'website_app/main.html', context=data)


# Страница команды
def connector_commands_page(request: HttpRequest, article_slug) -> HttpResponse:
    obj = get_object_or_404(Command, slug=article_slug)

    return render(request, 'website_app/command.html', context={'obj': obj, 'about': about, })


# Страница в случае отсутствия результата
def nof_found_page(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')
