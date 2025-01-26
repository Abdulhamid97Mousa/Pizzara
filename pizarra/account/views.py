from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email','')
        password = request.POST.get('password', '')
        
        if email and password:
            user = authenticate(request=request, email=email, password=password)
            if user is not None:
                auth_login(request,user)
        
                
                return redirect('/')
                
    return render(request, 'account/login.html')

# Create your views here.
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        
        if name and email and password1 and password2:
            user = User.objects.create_user(name=name, email=email, password=password1)
            
            return redirect('/login/')
        
    return render(request, 'account/signup.html')

@login_required
def logout(request):
    django_logout(request)
    return redirect('/')