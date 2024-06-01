from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("About/", views.aboutpage, name="about"),
]
