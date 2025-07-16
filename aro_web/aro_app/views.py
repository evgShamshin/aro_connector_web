from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from .models import Command, Group, Tag
from .forms import ConsultFormModel
from .utils import DataMixin


# Главная страница сайта
class ConnectorPage(DataMixin, ListView):
    template_name = 'aro_app/main.html'
    model = Command
    context_object_name = 'commands'
    descr = "Плагин Connector"

    def get_queryset(self):
        return Command.objects.filter(is_published=1).select_related('group').prefetch_related(
            Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Все команды"
        return context


# Главная страница с фильтрацией по категориям
class ConnectorPageByGroup(DataMixin, ListView):
    template_name = 'aro_app/main.html'
    model = Command
    context_object_name = 'commands'
    descr = "Плагин Connector"
    allow_empty = False

    def get_queryset(self):
        return Command.objects.filter(
            group=get_object_or_404(Group, slug=self.kwargs['group_slug']),
            is_published=1
        ).select_related('group').prefetch_related(
            Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_group'] = get_object_or_404(Group, slug=self.kwargs['group_slug'])
        context['title'] = f"Команды: {context['title_group'].title}"
        return context


# Главная страница с фильтрацией по тегам
class ConnectorPageByTag(DataMixin, ListView):
    template_name = 'aro_app/main.html'
    model = Command
    context_object_name = 'commands'
    descr = "Плагин Connector"

    def get_queryset(self):
        return Command.objects.filter(
            tag=get_object_or_404(Tag, slug=self.kwargs['tag_slug']),
            is_published=1
        ).select_related('group').prefetch_related(
            Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_tag'] = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
        context['title'] = f"Тег: {context['title_tag'].name}"
        return context


# Страница команды
def connector_commands_page(request: HttpRequest, article_slug) -> HttpResponse:
    data = {'title': 'ARO Group',
            'descr': """Плагин Connector - расширение для архитекторов и дизайнеров,
                                добавляющее возможности в Autodesk Revit.
                                Автоматизирует многие процессы и существенно сокращает время
                                создания модели.
                                Плагин совместим с 2019, 2020, 2021, 2022, 2023, 2024, 2025
                                версиями Autodesk Revit.""",
            'obj': get_object_or_404(Command, slug=article_slug),
            'commands': Command.objects.select_related('group').prefetch_related(
                Prefetch('tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')).
            filter(title=get_object_or_404(Command, slug=article_slug).title).
            values_list('tag__title', 'tag__slug'), }

    return render(request, 'aro_app/command.html', context=data)


# Страница консалтинга
class ConsultingPage(DataMixin, FormView):
    template_name = 'aro_app/consulting.html'
    descr = "BIM-консалтинг"
    form_class = ConsultFormModel
    success_url = reverse_lazy('connector')

    commands = Command.objects.select_related('group').prefetch_related(Prefetch(
        'tag', queryset=Tag.objects.all()[:1], to_attr='first_tag')).filter(is_published=1)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Страница в случае отсутствия результата
def nof_found_page(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>\n'
                                '<h3>Проверьте доступные url адреса в .urls</h3>')
