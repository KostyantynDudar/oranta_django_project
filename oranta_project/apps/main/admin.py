from django.contrib import admin
from django.utils.html import format_html, format_html_join
from .models import InsuranceApplication, UploadedFile
from django.utils.safestring import mark_safe


@admin.register(InsuranceApplication)
class InsuranceApplicationAdmin(admin.ModelAdmin):
    list_display = ('unique_code', 'phone_number', 'created_at', 'get_files')
    search_fields = ('unique_code', 'phone_number')
    list_filter = ('created_at',)

    def get_files(self, obj):
        all_files = UploadedFile.objects.filter(application=obj)
        if all_files.exists():
            return format_html_join(
                mark_safe('<br>'),
                '<a href="{}" target="_blank">Скачать {}</a>',
                ((file.file.url, file.file.name.split('/')[-1]) for file in all_files)
            )
        return format_html('<span style="color: red;">Нет файлов</span>')

    get_files.short_description = "Скачать файлы"
