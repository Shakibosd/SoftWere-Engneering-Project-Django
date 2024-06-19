from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash  
from django.contrib.auth.decorators import login_required   
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from .forms import RegisterForm


def home(request):
    return render(request, './home.html')

# def signup(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 messages.success(request,'Account Created Successfully!!!')
#                 form.save()
#                 print(form.cleaned_data)
#         else:
#             form = RegisterForm()
#         return render(request, './signup.html', {'form' : form})
#     else:
#         return redirect('profile')    

# add user signup class view
class SignupView(FormView):
    template_name = 'signup.html'  
    form_class = RegisterForm  
    success_url = reverse_lazy('profile')  

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account Created Successfully!!!')
        print(form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Form Is Invalid!!!')
        return super().form_invalid(form) 

# def user_login(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = AuthenticationForm(request=request, data = request.POST)
#             if form.is_valid():
#                 messages.success(request,'Account Created Successfully!!!')
#                 name = form.cleaned_data['username']    
#                 userpass = form.cleaned_data['password']
#                 user = authenticate(username = name, password = userpass)#check kortesi user database e ache kina
#                 if user is not None:
#                     login(request, user)
#                     return redirect('profile')#profile page e redirect korbe
#         else:
#             form = AuthenticationForm()
#         return render(request, './login.html', {'form' : form})
#     else:
#         return redirect('profile')


# add user login class view
class CustomLoginView(LoginView):
    template_name = './login.html'  
    redirect_authenticated_user = True  
    success_message = "Account Created Successfully!!!"  
    redirect_field_name = 'next'  

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile')


@login_required 
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request,'Account Update Successfully!!!')
                form.save()
        else:
            form = ChangeUserData(instance = request.user)
        return render(request, './profile.html', {'form' : form})
    else:
        return redirect('signup')


def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()     
                update_session_auth_hash(request, form.user)#password update korbe
                return redirect('profile')
            
        else:
            form = PasswordChangeForm(user=request.user)    
        return render(request,'./passchange.html', {'form' : form})
    else:
        return redirect('login')
    

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, './passchange.html', {'form': form})
    else:
        return redirect('login')
      

def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request,'Account Update Successfully!!!')
                form.save()
                print(form.cleaned_data)
         
        form = ChangeUserData()
        return render(request, './profile.html', {'form' : form})
    else:
        return redirect('signup')    

