from django.shortcuts import render
from . forms import contactForm

# Create your views here.   
def home(request):
    return render(request, './apps/home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './apps/about.html', {'name': name, 'email': email, 'select' : select})
    else:
        return render(request, './apps/about.html')

def submit_form(request):
    return render(request, './apps/form.html')


def djangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./apps/upload/'+file.name, 'wb+') as destination:
            #     for chunks in file.chunks():
            #         destination.write(chunks)
            print(form.cleaned_data)
    else:
        form = contactForm()   
    return render(request, './apps/django_form.html', {'form': form})    