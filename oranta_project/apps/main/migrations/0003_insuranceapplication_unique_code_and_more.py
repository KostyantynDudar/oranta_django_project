# Generated by Django 5.1.4 on 2024-12-23 23:12

import apps.main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_insuranceapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='insuranceapplication',
            name='unique_code',
            field=models.CharField(default=apps.main.models.generate_unique_code, max_length=20, unique=True, verbose_name='Уникальный код заявки'),
        ),
        migrations.AlterField(
            model_name='insuranceapplication',
            name='personal_docs',
            field=models.FileField(upload_to=apps.main.models.rename_personal_docs, verbose_name='Личные документы'),
        ),
        migrations.AlterField(
            model_name='insuranceapplication',
            name='tech_passport',
            field=models.FileField(upload_to=apps.main.models.rename_file, verbose_name='Техпаспорт'),
        ),
    ]