
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.set_section),
    path('get/', views.get_session),
    path('del/', views.delete_session),
]
