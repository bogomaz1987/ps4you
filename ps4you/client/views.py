from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from formtools.wizard.views import SessionWizardView

from client.forms import RegistrationClientForm
from client.functions import VerifyPhone


# class CreateClientView(SessionWizardView):
#     template_name = 'register.html'
#     step = '0'
#     request_id = None
#
#     def get_form_step_data(self, form):
#         if self.steps.current == self.step:
#             # TODO: add send sms with code for verify phone
#             self.request_id = VerifyPhone().send_code(phone=form.cleaned_data['phone'])
#             print(self.request_id)
#         return super().get_form_step_data(form)
#
#     def done(self, form_list, **kwargs):
#         print(form_list)
#         return HttpResponseRedirect(reverse('client_done'))

class RegistrationClientView(CreateView):
    form_class = RegistrationClientForm
    template_name = 'registration.html'

    def get_success_url(self):
        return reverse('mainpage')
