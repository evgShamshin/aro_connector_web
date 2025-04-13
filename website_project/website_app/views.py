from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .models import Command, About

about = About.objects.all()


def connector_page(request: HttpRequest):  # HttpResponse
    commands = Command.objects.all()

    data = {'title': 'Набор команд',
            'about': about,
            'commands': commands}
    return render(request, 'website_app/main.html', context=data)


def connector_commands_page(request: HttpRequest, article_slug) -> HttpResponse:
    obj = get_object_or_404(Command, slug=article_slug)
    return render(request, 'website_app/command.html', context={'obj': obj, 'about': about, })


def nof_found_page(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')
