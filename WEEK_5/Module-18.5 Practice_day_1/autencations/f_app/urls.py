
from django.urls import include, path   
from . import views

urlpatterns = [  
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('pass_change/', views.pass_change, name='pass_change'),
    path('pass_change2/', views.pass_change2, name='pass_change2'),
]
