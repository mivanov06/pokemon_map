from django.contrib import admin

from .models import Pokemon, PokemonEntity


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonEntity)
