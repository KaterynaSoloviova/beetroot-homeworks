# Generated by Django 5.1.2 on 2024-10-13 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250, verbose_name='Text')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Date Created')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
            ],
        ),
    ]
