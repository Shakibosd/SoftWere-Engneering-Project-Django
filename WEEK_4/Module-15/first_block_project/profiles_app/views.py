from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_profile(request):
    if request.method == 'POST': 
        profiles_form  = forms.ProfileForm(request.POST)
        if profiles_form.is_valid():
            profiles_form.save()
            return redirect('add_profiles')
    else:
        profiles_form = forms.ProfileForm()    
    return render(request, './profiles_app/add_profiles.html', {'form' : profiles_form})