# coding: utf-8

from django.db import models
from django.utils.translation import gettext as _


class Exchange(models.Model):
    game = models.ForeignKey('game.Game')
    client = models.ForeignKey('client.Client')
    exchange_games = models.ManyToManyField('game.Game', related_name='game')

    class Meta:
        verbose_name = _('Обмен')
        verbose_name_plural = _('Обмен')


class Sale(models.Model):
    game = models.ForeignKey('game.Game')
    client = models.ForeignKey('client.Client')
    price = models.IntegerField(verbose_name=_('Цена продажи'))

    class Meta:
        verbose_name = _('Продажа')
        verbose_name_plural = _('Продажи')


class Buy(models.Model):
    game = models.ForeignKey('game.Game')
    client = models.ForeignKey('client.Client')
    price = models.IntegerField(verbose_name=_('Цена продажи'))

    class Meta:
        verbose_name = _('Покупка')
        verbose_name_plural = _('Покупки')
