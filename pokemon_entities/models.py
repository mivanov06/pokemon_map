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

    class Meta:
        verbose_name = 'Координаты покемона'
        verbose_name_plural = 'Координаты покемонов'
