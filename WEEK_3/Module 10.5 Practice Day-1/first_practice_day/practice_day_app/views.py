from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    x = {'author' : 'shakib', 'age' : 5, 'lst' : ['Shakib', 'Is', 'Bed', 'But', 'She Tring', 'Good'], 'birthday' : datetime.datetime.now(), 'roll' : 10, 'title' : 'syed', 'val' : 'hi', 'lists' : [10,20,30,40,50,60,70,80,90,100],
    'cources' : [
          {
              'id' : 1,
              'name' : 'shakib',
              'fee' : 5000,
              'reg' : 12234244    
          },
          {
              'id' : 2,
              'name' : 'rakib',
              'fee' : 10040,
              'reg' : 12234245
          },
          {
              'id' : 3,
              'name' : 'nokib',
              'fee' : 10050,
              'reg' : 12234246
          },
          {
              'id' : 4,
              'name' : 'zillur',
              'fee' : 10090,
              'reg' : 12234247
          },
    ]}
         
    return render(request, 'home.html', x)