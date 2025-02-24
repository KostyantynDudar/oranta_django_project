# Generated by Django 5.1.4 on 2024-12-24 22:11

import apps.main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_insuranceapplication_unique_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=apps.main.models.rename_file, verbose_name='Файл')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.RemoveField(
            model_name='insuranceapplication',
            name='tech_passport',
        ),
        migrations.RemoveField(
            model_name='insuranceapplication',
            name='personal_docs',
        ),
        migrations.AddField(
            model_name='insuranceapplication',
            name='tech_passports',
            field=models.ManyToManyField(related_name='tech_passport_applications', to='main.uploadedfile', verbose_name='Техпаспорта'),
        ),
        migrations.AddField(
            model_name='insuranceapplication',
            name='personal_docs',
            field=models.ManyToManyField(related_name='personal_docs_applications', to='main.uploadedfile', verbose_name='Личные документы'),
        ),
    ]
