from django.contrib import admin, messages

from .models import Command, Group


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ('set_published', 'set_unpublished')

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