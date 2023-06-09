# Generated by Django 3.1.14 on 2023-03-23 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20230323_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='title',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_ru',
            field=models.CharField(default='', max_length=200, verbose_name='Название русское'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 18, 18, 51, 398307), verbose_name='Время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 18, 18, 51, 398307), verbose_name='Время исчезновения'),
        ),
    ]
