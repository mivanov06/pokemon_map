from datetime import datetime

from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='images', verbose_name='Изображение', blank=True, null=True)

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=1)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Время появления', default=datetime.now())
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения', default=datetime.now())
    level = models.IntegerField(verbose_name='Уровень', default=1)
    health = models.IntegerField(verbose_name='Здоровье', default=1)
    strength = models.IntegerField(verbose_name='Атака', default=1)
    defence = models.IntegerField(verbose_name='Защита', default=1)
    stamina = models.IntegerField(verbose_name='Выносливость', default=1)

    class Meta:
        verbose_name = 'Координаты покемона'
        verbose_name_plural = 'Координаты покемонов'
