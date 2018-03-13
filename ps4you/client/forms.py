from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from client.models import Client


class CreateClientForm(forms.ModelForm):
    username = forms.CharField(required=True, label='Имя', min_length=3, max_length=20)

    class Meta:
        model = Client
        fields = ('phone',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance')
    #     print(dir(instance.user))
    #     self.fields['username'].initial = instance.user.username


class PhonePassword(forms.Form):
    sms_password = forms.IntegerField(widget=forms.NumberInput, label='sms password')


# class ClientPasswordForm(forms.Form):
#     password = forms.CharField(widget=forms.CharField, label='password')
#     confirm_password = forms.CharField(widget=forms.CharField, label='confirm_password')
#
#     def clean(self):
#         cleaned_data = super().clean()
#         if self.cleaned_data.get('password') and self.cleaned_data.get('confirm_password') \
#                 and self.cleaned_data['password'] == self.cleaned_data['confirm_password']:
#             return cleaned_data
#         raise ValidationError(_('Password and Confirm password not the same'), code='invalid')
