from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request, 'Email or Password is incorrect!!!')
            return redirect('login')

    return render(request, 'login.html')


def RepetitionPage(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')

        
        
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'email is already exists!')
            return redirect('signup')
        else:
            my_user=User.objects.create_user(username=email,email=email,password=password)
            my_user.first_name = firstname
            my_user.last_name = lastname
            my_user.save()
            return redirect('login')
        
    
    return render(request, 'signup.html')


def LogOutPage(request):
    logout(request)

    return render(request, 'login.html')

