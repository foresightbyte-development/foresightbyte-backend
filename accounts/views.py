from accounts.models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import View


# Create your views here.

def SignInView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['login[password]']

        try:
            user = User.objects.get(email = email)
                    
            if user.check_password(password) :
                login(request, user)
                if user.is_sub:
                    return redirect('admin_dashboard')
                elif user.is_customer:
                    return redirect('admin_dashboard')
                elif user.is_superuser:
                    return redirect('admin_dashboard')
                else:
                    return render(request, 'admin/login.html')
                
            
        except User.DoesNotExist:
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

class SignOutView(LoginRequiredMixin, View):
    ''' Logoutview will logout the current login user '''

    def get(self, request):
        logout(request)
        return redirect('/')
