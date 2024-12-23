from django.contrib import admin
from django.urls import path, include
from apps.main.views import home_view, contact_view
from apps.main.views import submit_insurance_form
from apps.main import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),  # Главная страница
    path("contacts/", contact_view, name="contacts"),  # Контакты
    path('news/', include('news.urls')),  # Новости
    path('submit-form/', views.submit_insurance_form, name='submit_insurance_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)