from django.utils.html import format_html
from django.contrib import admin
from .models import InsuranceApplication

@admin.register(InsuranceApplication)
class InsuranceApplicationAdmin(admin.ModelAdmin):
    list_display = ('unique_code', 'phone_number', 'created_at', 'download_tech_passport', 'download_personal_docs')
    search_fields = ('unique_code', 'phone_number', 'tax_code', 'registration_address')

    def download_tech_passport(self, obj):
        if obj.tech_passport:
            return format_html('<a href="{}" download>Скачать</a>', obj.tech_passport.url)
        return "Нет файла"
    download_tech_passport.short_description = "Техпаспорт"

    def download_personal_docs(self, obj):
        if obj.personal_docs:
            return format_html('<a href="{}" download>Скачать</a>', obj.personal_docs.url)
        return "Нет файла"
    download_personal_docs.short_description = "Личные документы"
