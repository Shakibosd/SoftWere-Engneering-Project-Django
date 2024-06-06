from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('new/', views.musician_create, name='musician_create'),
    path('edit/<int:id>/', views.musician_edit, name='musician_edit'),
    path('delete/<int:id>/', views.musician_delete, name='musician_delete'),
]
