from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Musician/', include('Musician.urls')),
    path('Album/', include('Album.urls')),
    path('', include('Musician.urls')),  # Redirect home to musician list
]
    