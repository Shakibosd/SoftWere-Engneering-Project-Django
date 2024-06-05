from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('musician.urls')),  
    path('album/', include('Album.urls')),
    path('musician/', include('musician.urls')),
]


