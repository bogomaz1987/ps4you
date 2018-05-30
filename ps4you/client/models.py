from django.utils.translation import gettext as _

from user.models import User


class Client(User):
    class Meta:
        proxy = True
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')
