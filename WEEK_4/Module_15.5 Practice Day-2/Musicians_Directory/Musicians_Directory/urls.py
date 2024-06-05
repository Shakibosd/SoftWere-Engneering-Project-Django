from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('album/', include("Album.urls")),
    path('musician/', include("musician.urls")),
]


    