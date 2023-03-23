from django.db import models  # noqa F401


class Pokemon(models.Model):
    previous_evolution = models.ForeignKey('Pokemon', on_delete=models.SET_NULL, blank=True, null=True,
                                           verbose_name='Из кого эволюционировал',
                                           related_name='next_evolutions')
    title_ru = models.CharField(max_length=200, verbose_name='Название русское', blank=True)
    title_en = models.CharField(max_length=200, verbose_name='Название английское', blank=True)
    title_jp = models.CharField(max_length=200, verbose_name='Название японское', blank=True)
    description = models.TextField(max_length=1500, verbose_name='Описание', blank=True)
    image = models.ImageField(upload_to='images', verbose_name='Изображение', blank=True, null=True)

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон', related_name='entities')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Время появления', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения', null=True, blank=True)
    level = models.IntegerField(verbose_name='Уровень', null=True, blank=True)
    health = models.IntegerField(verbose_name='Здоровье', null=True, blank=True)
    strength = models.IntegerField(verbose_name='Атака', null=True, blank=True)
    defence = models.IntegerField(verbose_name='Защита', null=True, blank=True)
    stamina = models.IntegerField(verbose_name='Выносливость', null=True, blank=True)

    class Meta:
        verbose_name = 'Координаты покемона'
        verbose_name_plural = 'Координаты покемонов'

    def __str__(self):
        return self.pokemon.title_ru
