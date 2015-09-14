from django.conf.urls import patterns, url
from . import views
from . import views_api

urlpatterns = patterns('',
    url(r'^$', views.ContactListView.as_view(), name='contacts'),
    url(r'^new/$', views.ContactCreateView.as_view(), name='contacts_new'),
    url(r'^(?P<pk>\d+)$', views.ContactUpdateView.as_view(), name='contacts_edit'),
    url(r'^(?P<pk>\d+)/del$', views.ContactDeleteView.as_view(), name='contacts_delete'),
    url(r'^(?P<pk>\d+)/addr$', views.ContactAddressView.as_view(), name='contacts_address'),
    url(r'^(?P<pk>\d+)/phone$', views.ContactPhoneView.as_view(), name='contacts_phonenumber'),
    url(r'^(?P<pk>\d+)/email$', views.ContactEmailView.as_view(), name='contacts_email'),
    # ^api/locality/         - GET paginated filtered list of localities
    # ^api/locality/<pk>/    - GET a single locality by pk
    # ^api/state/            - GET paginated filtered list of states/provinces
    # ^api/state/<pk>/       - GET a single state by pk
    # ^api/country/          - GET paginated filtered list of countries
    url(r'api/country/$', views_api.CountryListView.as_view()),
    # ^api/country/<pk>/     - GET a single country by pk
    url(r'api/country/(?P<pk>\d+)/', views_api.CountryView.as_view()),
)
