
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('practice_day_app/', include('practice_day_app.urls')),
]
