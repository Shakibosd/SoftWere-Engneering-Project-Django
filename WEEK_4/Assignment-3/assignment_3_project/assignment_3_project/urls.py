from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('category_app.urls')),
    path('task/', include('task_app.urls')),
]
