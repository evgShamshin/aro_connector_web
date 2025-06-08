from django.contrib import admin
from django.urls import path, include
from website_app import urls as website_app_urls
from website_users import urls as website_users_urls

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('connector/admin/', admin.site.urls),
    path('', include(website_app_urls)),
    path('connector/users/', include(website_users_urls, namespace='users')), ]

admin.site.site_header = 'Администрирование сайта'
admin.site.index_title = 'Команды плагина ARO'
