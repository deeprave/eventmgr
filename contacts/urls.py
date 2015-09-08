from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.ContactListView.as_view(), name='contacts'),
    url(r'^new/$', views.ContactCreateView.as_view(), name='contacts_new'),
    url(r'^(?P<pk>\d+)$', views.ContactUpdateView.as_view(), name='contacts_edit'),
    url(r'^(?P<pk>\d+)/del$', views.ContactDeleteView.as_view(), name='contacts_delete'),
    url(r'^(?P<contact>\d+)/addr$', views.ContactCreateAddressView.as_view(), name='contacts_add_address'),
    url(r'^(?P<contact>\d+)/phone$', views.ContactCreatePhoneView.as_view(), name='contacts_add_phone'),
    url(r'^(?P<contact>\d+)/email$', views.ContactCreateEmailView.as_view(), name='contacts_add_email'),
)

