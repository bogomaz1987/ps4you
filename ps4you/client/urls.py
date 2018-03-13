from django.conf.urls import url
from django.views.generic import TemplateView
from client.forms import CreateClientForm, PhonePassword
from .views import CreateClientView

urlpatterns = [
    url(r'^$', CreateClientView.as_view([CreateClientForm, PhonePassword])),
    url(r'^profile/$', TemplateView.as_view(template_name='register_done.html'), name='client_done')
]
