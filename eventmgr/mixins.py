from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class LoginRequiredMixin(object):

    redirect_field_name = REDIRECT_FIELD_NAME
    login_url = None

    @method_decorator(login_required(redirect_field_name=redirect_field_name, login_url=login_url))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


""" derive generic views that have the login_required wrapper """


class ListViewLogin(LoginRequiredMixin, ListView):
    pass


class CreateViewLogin(LoginRequiredMixin, CreateView):
    pass


class UpdateViewLogin(LoginRequiredMixin, UpdateView):
    pass


class DeleteViewLogin(LoginRequiredMixin, DeleteView):
    pass

