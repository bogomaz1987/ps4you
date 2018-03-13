from django.contrib import admin

from game.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'rating_score', 'rating_people', 'logo_preview')
    search_fields = ('name',)
    list_filter = ('genres',)
    ordering = ['name']


