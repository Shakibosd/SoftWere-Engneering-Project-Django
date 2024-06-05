from django.shortcuts import render
from .forms import contactForm

def home(request):
    return render(request, 'home.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request, 'forms.html', {'form': form})
