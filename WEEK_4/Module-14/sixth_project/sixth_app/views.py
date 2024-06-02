from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    stdtnt = models.student.objects.all()
    return render(request,'./sixth_app/home.html', {'data' : stdtnt})  