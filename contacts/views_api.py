from django.http import HttpRequest
from nap.rest import views as rest_views
from nap.auth import permit_logged_in

from . import mappers
from . import models


class ApiAuthMixin(object):

    @permit_logged_in
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CountryListView(ApiAuthMixin, rest_views.BaseListView):
    model = models.Country
    mapper_class = mappers.CountryMapper


class CountryView(ApiAuthMixin, rest_views.ObjectGetMixin, rest_views.BaseObjectView):
    model = models.Country
    mapper_class = mappers.CountryMapper


class StateListView(rest_views.ListGetMixin, rest_views.BaseListView):
    model = models.State
    mapper_class = mappers.StateMapper


class LocalityListView(rest_views.ListGetMixin, rest_views.BaseListView):
    model = models.Locality
    mapper_class = mappers.LocalityMapper


