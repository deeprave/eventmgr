from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from eventmgr import mixins

from . import models
from . import forms


class ContactListView(mixins.ListViewLogin):
    model = models.Contact
    paginate_by = 25


class ContactCreateView(SuccessMessageMixin, mixins.CreateViewLogin):
    model = models.Contact
    form_class = forms.ContactForm
    success_url = reverse_lazy('contacts')
    success_message = "Contact '%(name)s' created successfully."


class ContactUpdateView(SuccessMessageMixin, mixins.UpdateViewLogin):
    model = models.Contact
    form_class = forms.ContactForm
    success_url = reverse_lazy('contacts')
    success_message = "Contact '%(name)s' updated successfully."


class ContactDeleteView(SuccessMessageMixin, mixins.DeleteViewLogin):
    model = models.Contact
    form_class = forms.ContactForm
    success_url = reverse_lazy('contacts')
    success_message = "Contact '%(name)s' deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class ContactAddressView(mixins.UpdateViewLogin):
    model = models.Contact
    form_class = forms.ContactAddressFormSet
    template_name = 'contacts/address_form.html'
    success_url = reverse_lazy('contacts')

    def get_success_url(self):
        return self.success_url


class ContactPhoneView(mixins.UpdateViewLogin):
    model = models.Contact
    form_class = forms.ContactPhoneFormSet
    template_name = 'contacts/phonenumber_form.html'
    success_url = reverse_lazy('contacts')

    def get_success_url(self):
        return self.success_url


class ContactEmailView(mixins.UpdateViewLogin):
    model = models.Contact
    form_class = forms.ContactEmailFormSet
    template_name = 'contacts/email_form.html'
    success_url = reverse_lazy('contacts')

    def get_success_url(self):
        return self.success_url

