from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    telegram = models.CharField(max_length=100, blank=True)
    viber = models.CharField(max_length=100, blank=True)
    skype = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(blank=True)
