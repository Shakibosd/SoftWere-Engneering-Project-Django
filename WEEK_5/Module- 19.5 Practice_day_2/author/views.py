from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash  
from django.contrib.auth.decorators import login_required   
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#home page
class HomeView(TemplateView):
    template_name = 'home.html'

#signup page
class SignupView(FormView):
    template_name = 'signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('signup')

    def form_valid(self, form):
        user = form.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')  
        user = authenticate(username=username, password=password)
        if user is not None:
            # login(self.request, user)
            messages.success(self.request, 'Account Created Successfully!!!')
        else:
            messages.error(self.request, 'Incorrect Information Please try again.')

        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('signup')
        return super().dispatch(request, *args, **kwargs)

#login page
class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

    def get_success_url(self):
        messages.success(self.request, 'Logged in successfully!!!')
        return reverse_lazy('profile')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)

#profile page
class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'profile.html'
    form_class = ChangeUserData
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account Updated Successfully!!!')
        return super().form_valid(form)

#logout page
def user_logout(request):
    logout(request)
    return redirect('login')

#password change page
class PasswordChangeView(LoginRequiredMixin, FormView):
    template_name = 'passchange.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, 'Password Changed Successfully!!!')
        return super().form_valid(form)
    
#password change without old password
class SetPasswordView(LoginRequiredMixin, FormView):
    template_name = 'passchange.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, 'Password Set Successfully!!!')
        return super().form_valid(form)
      
#change user data
class ChangeUserDataView(LoginRequiredMixin, FormView):
    template_name = 'profile.html'
    form_class = ChangeUserData
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account Updated Successfully!!!')
        return super().form_valid(form)