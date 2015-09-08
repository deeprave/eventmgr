from django.forms import models
from .models import Contact, Address, Email, PhoneNumber


class BootstrapForm(models.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        This is an ugly hack, but it works;
        way better than adding widgets for every field!
        """
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


class ContactForm(BootstrapForm):

    class Meta:
        model = Contact
        fields = ['title', 'name', 'nick', 'company']
        labels = {
            'nick': 'Nickname',
            'company': 'Company?'
        }
        help_texts = {
            'name': 'Contact\'s full name',
            'nick': 'Contact\'s nickname, or leave blank',
            'company': 'Check this if this contact is a company, not a person'
        }


class AddressForm(BootstrapForm):

    class Meta:
        model = Address
        fields = ['type', 'address_1', 'address_2', 'locality', 'title', 'contact_name']
        labels = {
            'type': 'Address Type',
            'title': 'Address Name',
            'contact_name': 'Address Contact'
        }
        help_texts = {
            'type': 'Select an appropriate address type',
            'address_1': 'Enter first address line (required)',
            'address_2': 'Enter second address line (optional)',
            'locality': 'Select the address locality',
            'title': 'Enter an optional name for this address or leave blank',
            'contact_name': 'Enter an optional contact name for this address',
        }


class EmailForm(BootstrapForm):

    class Meta:
        model = Email
        fields = ['address']
        labels = {
            'address': 'Email Address'
        }
        help_texts = {
            'address': 'Contact\'s email address in username@domain format'
        }


class PhoneForm(BootstrapForm):

    class Meta:
        model = PhoneNumber
        fields = ['phone_type', 'phone_number']
        labels = {
            'phone_type': 'Type',
            'phone_number': 'Phone Number'
        }
        help_texts = {
            'phone_type': 'Select an appropriate phone number type',
            'phone_number': 'Enter the phone number (localised or with +country prefix)',
        }
