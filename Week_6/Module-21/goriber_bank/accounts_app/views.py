from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import userRagisterForm
from django.views.generic import FormView
from django.contrib.auth import login
# Create your views here.

class userRagisterView(FormView):
    template_name = 'accounts_app/user_register.html'
    form_class = userRagisterForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)


