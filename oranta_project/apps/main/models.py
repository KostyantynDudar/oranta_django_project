# Файл: /home/oranta_django_project/oranta_project/apps/main/models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class InsuranceApplication(models.Model):
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    tax_code = models.CharField(max_length=10, verbose_name="Налоговый код")
    tech_passport = models.FileField(upload_to="tech_passports/", verbose_name="Техпаспорт")
    personal_docs = models.FileField(upload_to="personal_docs/", verbose_name="Личные документы")
    registration_address = models.TextField(verbose_name="Адрес регистрации")
    deductible = models.CharField(
        max_length=10,
        choices=[
            ('0', '0 грн'),
            ('1500', '1500 грн'),
            ('2500', '2500 грн')
        ],
        verbose_name="Франшиза"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи заявки")

    def __str__(self):
        return f"Заявка от {self.phone_number} ({self.created_at})"

