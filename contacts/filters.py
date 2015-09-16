from django_filters import FilterSet

from .models import Country, State, Locality, Contact


class ContactFilter(FilterSet):

    class Meta:
        model = Contact
        fields = {
            'name': ['icontains'],
            'nick': ['icontains']
        }


class CountryFilter(FilterSet):

    class Meta:
        model = Country
        fields = {
            'abbrev' : ['icontains'],
            'name': ['icontains']
        }


class StateFilter(FilterSet):

    class Meta:
        model = State
        fields = {
            'country__abbrev': ['exact'],
            'abbrev': ['icontains'],
            'name': ['icontains']
        }

class LocalityFilter(FilterSet):

    class Meta:
        model = Locality
        fields = {
            'state__country__abbrev': ['exact'],
            'state__abbrev': ['exact'],
            'name': ['icontains'],
            'postcode': ['exact']
        }

