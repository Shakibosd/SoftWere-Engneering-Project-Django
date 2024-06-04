from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home(request):
    stdtnt = models.student.objects.all()
    return render(request,'./sixth_app/home.html', {'data' : stdtnt})  


def deleteStudent(request, roll):
    std = models.student.objects.get(pk = roll).delete()
    return redirect("home")
    