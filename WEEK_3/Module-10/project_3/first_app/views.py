from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'author' : 'rohim', 'age' : '15', 'lst' : [1,2,3]}
    return render(request, 'home.html', d)
