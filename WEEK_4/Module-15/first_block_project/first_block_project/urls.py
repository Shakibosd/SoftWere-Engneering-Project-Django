
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('author_app/',include('author_app.urls')),
    path('categories_app/',include('categories_app.urls')),
    path('post_app/',include('post_app.urls')),
    path('profiles_app/',include('profiles_app.urls')),
]
