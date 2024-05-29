
from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'author' : 'rohim', 'age' : 15, 'lst' : ['python','is','best'], 'birthday' : datetime.datetime.now(), 'val' : '', 'courses' : [

        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'django',
            'fee' : 10000
        },
        {
            'id' : 3,
            'name' : 'c',
            'fee' : 1000
        },
    ]}
    return render(request, 'home.html', d)
