from django.db import models
import os
from uuid import uuid4
from datetime import datetime

def rename_file(instance, filename):
    ext = filename.split('.')[-1]
    identifier = instance.application.unique_code if hasattr(instance, 'application') else uuid4().hex[:6]
    filename = f"{identifier}_{uuid4().hex[:6]}.{ext}"
    return os.path.join('uploaded_files/', filename)


def rename_personal_docs(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.unique_code}_Личные_документы.{ext}"
    return os.path.join('personal_docs/', filename)


def generate_unique_code():
    return datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid4().hex[:6])

class UploadedFile(models.Model):
    application = models.ForeignKey(
        'InsuranceApplication', 
        on_delete=models.CASCADE, 
        related_name="uploaded_files", 
        null=True, 
        blank=True, 
        verbose_name="Заявка"
    )
    file = models.FileField(upload_to=rename_file, verbose_name="Файл")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} (Заявка: {self.application.unique_code if self.application else 'Нет заявки'})"



class InsuranceApplication(models.Model):
    unique_code = models.CharField(max_length=20, unique=True, default=generate_unique_code, verbose_name="Уникальный код заявки")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    tax_code = models.CharField(max_length=10, verbose_name="Налоговый код")
    tech_passports = models.ManyToManyField(UploadedFile, related_name="tech_passport_applications", verbose_name="Техпаспорта")
    personal_docs = models.ManyToManyField(UploadedFile, related_name="personal_docs_applications", verbose_name="Личные документы")
    registration_address = models.TextField(verbose_name="Адрес регистрации")
    deductible = models.CharField(
        max_length=10,
        choices=[('0', '0 грн'), ('1500', '1500 грн'), ('2500', '2500 грн')],
        verbose_name="Франшиза"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи заявки")

    def __str__(self):
        return f"Заявка {self.unique_code} от {self.phone_number}"
