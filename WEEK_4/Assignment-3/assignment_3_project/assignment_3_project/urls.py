from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('task_app/', include('task_app.urls')),
    path('category_app/', include('category_app.urls')),
]
