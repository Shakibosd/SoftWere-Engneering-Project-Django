from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('new/', views.album_create, name='album_create'),
    path('edit/<int:id>/', views.album_edit, name='album_edit'),
    path('delete/<int:id>/', views.album_delete, name='album_delete'),
]
