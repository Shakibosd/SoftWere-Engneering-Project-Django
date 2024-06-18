from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('Musician/', include('Musician.urls')),
    path('Album/', include('Album.urls')), 
    path('Author/', include('author.urls')), 
]
    