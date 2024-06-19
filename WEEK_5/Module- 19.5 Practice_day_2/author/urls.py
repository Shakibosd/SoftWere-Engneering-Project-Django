from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('signup/', views.signup, name = 'signup'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    # path('login/', views.user_login, name = 'login'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('profile/', views.profile, name = 'profile'),
    path('logout/', views.user_logout, name = 'logout'),
    path('pass_change/', views.pass_change, name = 'pass_change'),
    path('pass_change2/', views.pass_change2, name='pass_change2'),
]

