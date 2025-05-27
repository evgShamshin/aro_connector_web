from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .models import Command, About, Group, Tag, Consult
# from .forms import ConsultForm
from .forms import ConsultFormModel


# Главная страница сайта
def connector_page(request: HttpRequest) -> HttpResponse:
    data = {'title': 'ARO Group',
            'descr': """Плагин Connector - расширение для архитекторов и дизайнеров,
                        добавляющее возможности в Autodesk Revit.
                        Автоматизирует многие процессы и существенно сокращает время
                        создания модели.
                        Плагин совместим с 2019, 2020, 2021, 2022, 2023, 2024, 2025
                        версиями Autodesk Revit.""",
            'about': About.objects.all(),
            'commands': Command.objects.select_related('group').prefetch_related(
                Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')).filter(is_published=1),
            'tags': Tag.objects.all(),
            'groups': Group.objects.all()}

    return render(request, 'website_app/main.html', context=data)


# Главная страница с фильтрацией по категориям
def connector_page_by_group(request: HttpRequest, group_slug) -> HttpResponse:
    data = {'title': 'ARO Group',
            'descr': """Плагин Connector - расширение для архитекторов и дизайнеров,
                            добавляющее возможности в Autodesk Revit.
                            Автоматизирует многие процессы и существенно сокращает время
                            создания модели.
                            Плагин совместим с 2019, 2020, 2021, 2022, 2023, 2024, 2025
                            версиями Autodesk Revit.""",
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

    data = {'title': 'ARO Group',
            'descr': """Плагин Connector - расширение для архитекторов и дизайнеров,
                            добавляющее возможности в Autodesk Revit.
                            Автоматизирует многие процессы и существенно сокращает время
                            создания модели.
                            Плагин совместим с 2019, 2020, 2021, 2022, 2023, 2024, 2025
                            версиями Autodesk Revit.""",
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
    data = {'title': 'ARO Group',
            'descr': """Плагин Connector - расширение для архитекторов и дизайнеров,
                                добавляющее возможности в Autodesk Revit.
                                Автоматизирует многие процессы и существенно сокращает время
                                создания модели.
                                Плагин совместим с 2019, 2020, 2021, 2022, 2023, 2024, 2025
                                версиями Autodesk Revit.""",
            'about': About.objects.all(),
            'groups': Group.objects.all(),
            'tags': Tag.objects.all(),
            'obj': get_object_or_404(Command, slug=article_slug),
            'commands': Command.objects.select_related('group').prefetch_related(
                Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')).
            filter(title=get_object_or_404(Command, slug=article_slug).title).
            values_list('tag__title', 'tag__slug'), }

    return render(request, 'website_app/command.html', context=data)


# Страница консалтинга
def consulting_page(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ConsultFormModel(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            print(request.FILES)
            try:
                Consult.objects.create(**form.cleaned_data)
                return redirect("connector")
            except:
                form.add_error(None, form.errors)
    else:
        form = ConsultFormModel()

    data = {'title': 'ARO Group',
            'descr': """BIM-консалтинг - это комплекс услуг по внедрению,
                        адаптации и оптимизации технологий информационного моделирования
                        (BIM) на всех этапах жизненного цикла строительного проекта.
                        Мы помогаем компаниям повысить эффективность работы,
                        сократить сроки проектирования и минимизировать ошибки
                        за счёт грамотного использования современных цифровых инструментов.""",
            'about': About.objects.all(),
            'commands': Command.objects.select_related('group').prefetch_related(
                Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')).
            filter(is_published=1),
            'tags': Tag.objects.all(),
            'groups': Group.objects.all(),
            'form': form, }

    return render(request, 'website_app/consulting.html', context=data)


# Страница в случае отсутствия результата
def nof_found_page(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')
