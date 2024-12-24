# Файл: /home/oranta_django_project/oranta_project/apps/main/models.py

from django.db import models
from django.utils.timezone import now
from uuid import uuid4
import os


def rename_file(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.unique_code}_Техпаспорт.{ext}"
    return os.path.join('tech_passports/', filename)


def rename_personal_docs(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.unique_code}_Личные_документы.{ext}"
    return os.path.join('personal_docs/', filename)


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

def generate_unique_code():
    from datetime import datetime
    from uuid import uuid4
    return datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid4().hex)[:6]

class InsuranceApplication(models.Model):
    unique_code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Уникальный код заявки",
        default=generate_unique_code  # Указываем функцию вместо lambda
    )
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    tax_code = models.CharField(max_length=10, verbose_name="Налоговый код")
    tech_passport = models.FileField(upload_to=rename_file, verbose_name="Техпаспорт")
    personal_docs = models.FileField(upload_to=rename_personal_docs, verbose_name="Личные документы")
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

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = generate_unique_code()
        super().save(*args, **kwargs)
