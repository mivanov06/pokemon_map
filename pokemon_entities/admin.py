from django.contrib import admin

from .models import Pokemon, PokemonEntity


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ('pokemon', 'latitude', 'longitude', 'level', 'appeared_at', 'disappeared_at')


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonEntity, PokemonEntityAdmin)
