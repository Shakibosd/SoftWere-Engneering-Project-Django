from django.shortcuts import render


# Create your views here.
def homepage(req):
    return render(req, "mainapp/home.html")


def aboutpage(req):
    return render(req, "mainapp/about.html")
