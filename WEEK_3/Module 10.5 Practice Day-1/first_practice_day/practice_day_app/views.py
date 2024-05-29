from django.shortcuts import render
import datetime

# Create your views here.

def home(request):

    x = {'author' : 'shakib', 'age' : 5, 'lst' : ['shakib', 'is', 'bed'], 'birthday' : datetime.datetime.now(),
    'cources' : [
          {
              'id' : 1,
              'name' : 'shakib',
              'fee' : 5000
          },
          {
              'id' : 2,
              'name' : 'rakib',
              'fee' : 10040
          },
          {
              'id' : 3,
              'name' : 'nokib',
              'fee' : 10050
          },
    ]}
         
    return render(request, 'home.html', x)