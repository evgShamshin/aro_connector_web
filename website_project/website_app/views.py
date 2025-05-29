from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from .models import Command, About, Group, Tag, Consult
from .forms import ConsultFormModel
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView


# Главная страница сайта
class ConnectorPage(TemplateView):
    template_name = 'website_app/main.html'
    extra_context = {'title': 'ARO Group',
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


# Главная страница с фильтрацией по категориям
class ConnectorPageByGroup(ListView):
    model = Command
    template_name = 'website_app/main.html'
    context_object_name = 'commands'
    allow_empty = False

    def get_queryset(self):
        return Command.objects.filter(
            group=get_object_or_404(Group, slug=self.kwargs['group_slug'])).select_related('group').prefetch_related(
            Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')).filter(is_published=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'ARO Group'
        context['descr'] = """Плагин Connector - расширение для архитекторов и дизайнеров,
                             добавляющее возможности в Autodesk Revit.
                             Автоматизирует многие процессы и существенно сокращает время
                             создания модели.
                             Плагин совместим с 2019, 2020, 2021, 2022, 2023, 2024, 2025
                             версиями Autodesk Revit."""
        context['title_group'] = Group.objects.filter(slug=self.kwargs['group_slug']).get()
        context['about'] = About.objects.all()
        context['groups'] = Group.objects.all()
        context['tags'] = Tag.objects.all()
        return context


# Главная страница с фильтрацией по тегам
class ConnectorPageByTag(ListView):
    model = Command
    template_name = 'website_app/main.html'
    context_object_name = 'commands'

    def get_queryset(self):
        return Command.objects.filter(tag=self.kwargs['tag_slug']).select_related('group').prefetch_related(
            Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')
        ).filter(is_published=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'ARO Group'
        context['descr'] = """Плагин Connector - расширение для архитекторов и дизайнеров,
                                     добавляющее возможности в Autodesk Revit.
                                     Автоматизирует многие процессы и существенно сокращает время
                                     создания модели.
                                     Плагин совместим с 2019, 2020, 2021, 2022, 2023, 2024, 2025
                                     версиями Autodesk Revit."""
        context['title_tag'] = Tag.objects.filter(slug=self.kwargs['tag_slug']).get()
        context['about'] = About.objects.all()
        context['groups'] = Group.objects.all()
        context['tags'] = Tag.objects.all()
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
        return context


# def connector_page_by_tag(request: HttpRequest, tag_slug) -> HttpResponse:
#     tag = get_object_or_404(Tag, slug=tag_slug)
#
#     data = {'title': 'ARO Group',
#             'descr': """Плагин Connector - расширение для архитекторов и дизайнеров,
#                             добавляющее возможности в Autodesk Revit.
#                             Автоматизирует многие процессы и существенно сокращает время
#                             создания модели.
#                             Плагин совместим с 2019, 2020, 2021, 2022, 2023, 2024, 2025
#                             версиями Autodesk Revit.""",
#             'title_tag': Tag.objects.filter(slug=tag_slug).get(),
#             'about': About.objects.all(),
#             'groups': Group.objects.all(),
#             'tags': Tag.objects.all(),
#             'tag': get_object_or_404(Tag, slug=tag_slug),
#             'commands': Command.objects.filter(tag=tag)  # Фильтруем команды по тегу
#             .select_related('group')  # Оптимизация для ForeignKey
#             .prefetch_related(
#                 Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')
#             ).filter(is_published=1), }
#
#     return render(request, 'website_app/main.html', context=data)


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
class ConsultingPage(View):
    def get(self, request):
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

        return render(request, 'website_app/consulting.html', data)

    def post(self, request):
        form = ConsultFormModel(request.POST, request.FILES)
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

        if form.is_valid():
            print(form.cleaned_data)
            print(request.FILES)
            try:
                Consult.objects.create(**form.cleaned_data)
                return redirect("connector")
            except:
                form.add_error(None, form.errors)

        return render(request, 'website_app/consulting.html', data)


# Страница в случае отсутствия результата
def nof_found_page(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')
