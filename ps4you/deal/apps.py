# coding: utf-8

from django.apps import AppConfig
from django.utils.translation import gettext as _


class SaleConfig(AppConfig):
    name = 'deal'
    verbose_name = _('Сделаки')

