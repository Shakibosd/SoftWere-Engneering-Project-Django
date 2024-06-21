
from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post_app.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from payment_app.models import PaymentModel
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, './author_app/register.html', {'form' : register_form, 'type' : 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
        else:
            messages.warning(request, 'You have entered wrong logging information, log in with correct information, register if not registered.')
            return redirect('user_login')   
    else:
        form = AuthenticationForm()
        return render(request, './author_app/register.html', {'form' : form, 'type' : 'Login'})


@login_required 
def profile(request):
    data = Post.objects.filter(author = request.user)
    historie = PaymentModel.objects.all()
    return render(request, './author_app/profile.html',context={'data' : data,"historie":historie})      


@login_required 
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Update Successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request, './author_app/update_profile.html', {'form' : profile_form})       


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, './author_app/pass_change.html', {'form' : form})


def user_logout(request):
    logout(request)
    return redirect('user_login')


# add class views user login
class UserLoginView(LoginView):
    template_name = './author_app/register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successfull!!!')
        return super().form_valid(form) 
    
    def form_invalid(self, form):
        messages.success(self.request, 'LoggedIn Information Incorect!!!')
        return super().form_invalid(form) 

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['type'] = 'Login'
        return contex
        