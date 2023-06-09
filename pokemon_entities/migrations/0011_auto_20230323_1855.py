# Generated by Django 3.1.14 on 2023-03-23 08:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_auto_20230323_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='Из кого эволюционировал'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 18, 55, 36, 330222), verbose_name='Время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 18, 55, 36, 330222), verbose_name='Время исчезновения'),
        ),
    ]
