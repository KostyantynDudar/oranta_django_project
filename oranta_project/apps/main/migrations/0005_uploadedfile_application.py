# Generated by Django 5.1.4 on 2024-12-24 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_uploadedfile_delete_article_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_files', to='main.insuranceapplication', verbose_name='Заявка'),
        ),
    ]
