#! -*- coding: utf-8 -*-

from django.utils.translation import gettext as _
from django.db import models


class Genre(models.Model):
    name = models.CharField(verbose_name=_('Жанр игры'), max_length=150, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(verbose_name=_('Название'), max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.name


class GameContentType(models.Model):
    name = models.CharField(verbose_name=_('Тип игры'), max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(verbose_name=_('Название'), max_length=300, unique=True, db_index=True)
    ps_id = models.CharField(verbose_name=_('Уникальный идентификатор'), max_length=300, db_index=True)
    release_date = models.DateField(verbose_name=_('Дата рализа'), db_index=True, null=True)
    genres = models.ManyToManyField(verbose_name=_('Жанр игры'), to=Genre, db_index=True)
    content_type = models.ForeignKey(verbose_name=_('Тип игры'), to=GameContentType, null=True)
    platforms = models.ManyToManyField(verbose_name=_('Платформы'), to=Platform, db_index=True)
    rating_score = models.FloatField(verbose_name=_('Рейтинг'), db_index=True, default=0, null=True)
    rating_people = models.IntegerField(verbose_name=_('Людей проголосовало'), db_index=True, default=0, null=True)
    page = models.CharField(verbose_name=_('Страница игры в ps store'), max_length=300)
    logo = models.CharField(verbose_name=_('Лого игры'), max_length=300)

    def __str__(self):
        return self.name

    def logo_preview(self):
        return '<a href=%s><img src="%s" height="50"/></a>' % (self.logo, self.logo)
    logo_preview.allow_tags = True

    class Meta:
        index_together = (
            ('release_date', 'rating_score'),
            ('release_date', 'rating_score', 'rating_people'),
            ('name', 'release_date', 'rating_score', 'rating_people'),
        )


class Price(models.Model):
    game = models.ForeignKey('game.Game', verbose_name=_('Игра'))
    price_plus_user = models.IntegerField(verbose_name=_('Цена для ps plus'), db_index=True, null=True)
    price_non_plus_user = models.IntegerField(verbose_name=_('Цена для всех'), db_index=True, null=True)
    date = models.DateField(verbose_name=_('Дата сохранения цены'), auto_now_add=True, db_index=True)
