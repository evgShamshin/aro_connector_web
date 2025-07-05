from django.contrib import admin, messages
from django.db.models import Q
from django.db.models.functions import Length

from .models import Command, Group


class ContentFilter(admin.SimpleListFilter):
    title = 'Описание'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [('short', 'Короткое'),
                ('middle', 'Среднее'),
                ('long', 'Длинное')]

    def queryset(self, request, queryset):
        queryset = queryset.annotate(length=Length('description'))

        if self.value() == 'short':
            return queryset.filter(length__lt=10)
        if self.value() == 'middle':
            return queryset.filter(Q(length__gte=10)
                                   & Q(length__lt=50))
        if self.value() == 'long':
            return queryset.filter(length__gte=50)


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'group', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ('set_published', 'set_unpublished')
    search_fields = ('title', 'group__title')
    list_filter = ('is_published', 'group__title', ContentFilter)

    @admin.action(description='Опубликовать выбранные Команды')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Command.Status.PUBLISHED)
        self.message_user(request, f'Опубликованы {count} Команд', messages.SUCCESS)

    @admin.action(description='Убрать в разработку выбранные Команды')
    def set_unpublished(self, request, queryset):
        count = queryset.update(is_published=Command.Status.DRAFT)
        self.message_user(request, f'Убраны {count} Команд', messages.WARNING)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
