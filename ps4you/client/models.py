# coding: utf-8

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram = models.CharField(max_length=100, default=None, null=True, blank=True)
    viber = models.CharField(max_length=100, default=None, null=True, blank=True)
    skype = models.CharField(max_length=100, default=None, null=True, blank=True)
    phone = models.CharField(max_length=100, default=None, null=True, blank=True)

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')
