from django.urls import reverse
from django.views.generic import CreateView

from client.forms import RegistrationClientForm


class RegistrationClientView(CreateView):
    form_class = RegistrationClientForm
    template_name = 'registration.html'

    def get_success_url(self):
        return reverse('mainpage')
