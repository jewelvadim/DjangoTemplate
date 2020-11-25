# Generated by Django 2.2 on 2020-08-05 10:01

from django.db import migrations, models

import ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Вместо удаления элемента, снимите эту галочку', verbose_name='Активный?')),
                ('email', models.EmailField(max_length=100, verbose_name='Почтовый адрес')),
            ],
            options={
                'verbose_name': 'Почтовый адрес',
                'verbose_name_plural': 'Почтовые адреса',
            },
        ),
        migrations.CreateModel(
            name='MainConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_robots', models.BooleanField(default=False, verbose_name='Разрешить индексацию?', help_text='Если галочка не активна, поисковые роботы не будут индексировать сайт')),
                ('extra_scripts', models.TextField(blank=True, verbose_name='Дополнительные скрипты')),
                ('policy', ckeditor.fields.RichTextField(blank=True, verbose_name='Политика конфиденциальности')),
            ],
            options={
                'verbose_name': 'Глобальные настройки',
                'verbose_name_plural': 'Глобальные настройки',
            },
        ),
        migrations.CreateModel(
            name='SeoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(blank=True, max_length=70, verbose_name='СЕО-заголовок')),
                ('seo_description', models.TextField(blank=True, max_length=140, verbose_name='СЕО-описание')),
                ('path', models.CharField(help_text='/section/item/', max_length=150, unique=True, verbose_name='Путь')),
            ],
            options={
                'verbose_name': 'Элемент сео',
                'verbose_name_plural': 'Элементы сео',
            },
        ),
    ]