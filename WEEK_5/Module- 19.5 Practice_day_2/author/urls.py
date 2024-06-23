
from . import views
from django.urls import path
from .views import HomeView, SignupView, CustomLoginView, ProfileView, PasswordChangeView, SetPasswordView, ChangeUserDataView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_change/', PasswordChangeView.as_view(), name='pass_change'),
    path('set_password/', SetPasswordView.as_view(), name='pass_change2'),
    path('change_user_data/', ChangeUserDataView.as_view(), name='change_user_data'),
]
