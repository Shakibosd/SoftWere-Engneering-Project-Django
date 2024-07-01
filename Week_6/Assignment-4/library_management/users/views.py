from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from  django.views.generic import CreateView
from Books.views import send_transaction_email
from .forms import RegistreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DepositeForm
from .models import Deposite, UserBankAccount

class RegistrationView(CreateView):
    model=User
    form_class=RegistreationForm
    template_name='signup.html'
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        messages.success(self.request,f'Your account Successfully Created')
        return super().form_valid(form)
    def get_context_data(self,*args, **kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['type']='Registration'
        return context

class UserLoginView(LoginView):
    template_name='login.html'
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self,form):
        messages.success(self.request,'Logdin Successfully!!!')
        return super().form_valid(form)
    
    def form_invalid(slef,form):
        return super().form_invalid(form)
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['type']='Login'
        return context 
    
class UserLogoutView(LoginRequiredMixin,LogoutView):
    model=User
    def get_success_url(self):
        return reverse_lazy('home')
    

class DeposteView(LoginRequiredMixin,CreateView):
    model=Deposite
    form_class=DepositeForm
    template_name='deposite.html'
    success_url=reverse_lazy('home')
    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs.update(
            {'account':self.request.user.account}
        )
        return kwargs
    
    def form_valid(self,form):
        amount=form.cleaned_data.get('amount')
        account=self.request.user.account
        account.balance+=amount
        account.save(
            update_fields=[
                'balance'
            ]
        )
        messages.success(self.request,f'Your Deposite Amount {amount}$ Successflly!!!')

        send_transaction_email(self.request.user, amount, 'Deposit Message', 'deposite_email.html')

        return super().form_valid(form)
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Deposite Money'
        return context
    
