from django.contrib import admin
from django import forms
from searchableselect.widgets import SearchableSelect

from deal.models import Buy, Sale, Exchange
from game.models import Game


@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    fields = ['game', 'price']

    def save_model(self, request, obj, form, change):
        obj.client = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    fields = ['game', 'price']

    def save_model(self, request, obj, form, change):
        obj.client = request.user
        return super().save_model(request, obj, form, change)


class TravelerForm(forms.ModelForm):
    class Meta:
        model = Exchange
        exclude = ()
        widgets = {
            'cities_visited': SearchableSelect(model='game.Game', search_field='name', many=True, limit=10)
        }

# @admin.register(Exchange)
# class ExchangeAdmin(admin.ModelAdmin):
#     fields = ['game', 'exchange_games']
#     form = TravelerForm
#
#     def save_model(self, request, obj, form, change):
#         obj.client = request.user.client
#         return super().save_model(request, obj, form, change)

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    fields = ['game', 'exchange_games']
    form = TravelerForm
