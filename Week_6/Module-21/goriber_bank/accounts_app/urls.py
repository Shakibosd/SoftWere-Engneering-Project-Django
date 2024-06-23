
from django.urls import path, include
from .views import userRagisterView

urlpatterns = [
    path('register/', userRagisterView.as_view(), name='register'),
]
