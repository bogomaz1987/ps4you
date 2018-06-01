from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from client.forms import CreateClientForm, PhonePassword
from .views import RegistrationClientView

urlpatterns = [
    # url(r'^$', CreateClientView.as_view([CreateClientForm, PhonePassword])),
    # url(r'^profile/$', TemplateView.as_view(template_name='register_done.html'), name='client_done')
    path('register/', RegistrationClientView.as_view(), name='registration_client')
]
