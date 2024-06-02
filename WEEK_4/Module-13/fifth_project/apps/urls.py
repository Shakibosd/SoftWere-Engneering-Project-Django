
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('form/', views.submit_form, name='submit_form'),
    # path('django_form/', views.studentForm, name='django_form'),
    path('django_form/', views.passwordValidation, name='django_form'),
    # path('django_form/', views.djangoForm, name='django_form'),
]
    