from django.contrib import admin
from django.urls import path
from apps.main.views import home_view, contact_view, article_list_view, article_detail_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),  # Главная страница
    path("contacts/", contact_view, name="contacts"),  # Контакты
    path("articles/", article_list_view, name="articles"),  # Список статей
    path("articles/<int:id>/", article_detail_view, name="article_detail"),  # Детальная статья
]
