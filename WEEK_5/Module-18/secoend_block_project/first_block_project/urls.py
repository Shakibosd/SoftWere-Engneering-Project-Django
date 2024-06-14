
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.home, name='category_wise_post'),
    path('author_app/',include('author_app.urls')),
    path('categories_app/',include('categories_app.urls')),
    path('post_app/',include('post_app.urls')),
]
