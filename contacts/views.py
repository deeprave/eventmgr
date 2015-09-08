from django.core.urlresolvers import reverse_lazy
from eventmgr.mixins import ListViewLogin, CreateViewLogin, UpdateViewLogin, DeleteViewLogin
from .models import Contact, Address, PhoneNumber, Email
from .forms import ContactForm, AddressForm, EmailForm, PhoneForm


class ContactListView(ListViewLogin):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactCreateView(CreateViewLogin):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts')


class ContactUpdateView(UpdateViewLogin):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts')


class ContactDeleteView(DeleteViewLogin):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts')


class ContactCreateAddressView(CreateViewLogin):
    model = Address
    form_class = AddressForm
    success_url = reverse_lazy('contacts')


class ContactCreatePhoneView(CreateViewLogin):
    model = PhoneNumber
    form_class = PhoneForm
    success_url = reverse_lazy('contacts')


class ContactCreateEmailView(CreateViewLogin):
    model = Email
    form_class = EmailForm
    success_url = reverse_lazy('contacts')
