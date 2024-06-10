from django.shortcuts import render
from . forms import RegisterForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account Created Successfully')
            form.save()
            print(form.cleaned_data)
    else:        
        form = RegisterForm()
    return render(request, 'home.html')

