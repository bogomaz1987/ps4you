from django.http import HttpResponseRedirect
from django.urls import reverse
from formtools.wizard.views import SessionWizardView
from client.functions import VerifyPhone


class CreateClientView(SessionWizardView):
    template_name = 'register.html'
    step = '0'
    request_id = None

    def get_form_step_data(self, form):
        if self.steps.current == self.step:
            # TODO: add send sms with code for verify phone
            self.request_id = VerifyPhone().send_code(phone=form.cleaned_data['phone'])
            print(self.request_id)
        return super().get_form_step_data(form)

    def done(self, form_list, **kwargs):
        print(form_list)
        return HttpResponseRedirect(reverse('client_done'))
