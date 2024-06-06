from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def category(request):
    return render(request, 'category.html')
