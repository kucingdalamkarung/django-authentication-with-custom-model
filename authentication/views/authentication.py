from django.views import generic
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from .. import forms


class LoginView(generic.FormView):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        credentials = form.cleaned_data
        user = authenticate(username=credentials['email'], password=credentials['password'])
        print(user)

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            return HttpResponseRedirect(reverse_lazy('authentication:login'))


class RegisterView(generic.FormView):
    form_class = forms.RegisterForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home'))
