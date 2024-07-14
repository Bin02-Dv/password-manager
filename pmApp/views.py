from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import (
    MyPasswords
)

def logout(request):
    auth.logout(request)
    return redirect('/')


def signin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if confirm_password != password:
            messages.error(request, "Pssword and confirm password missed match!!")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exist!!")      
        else:
            new_user = User.objects.create_user(username=email, email=email, first_name=fullname, password=password)
            new_user.save()
            return redirect('/')
    return render(request, 'register.html')

@login_required(login_url='/')
def dashboard(request):
    current_user = User.objects.get(username=request.user)
    return render(request, 'index.html', {"user": current_user})

@login_required(login_url='/')
def mypass(request):
    current_user = User.objects.get(username=request.user)
    passwords = MyPasswords.objects.filter(user=current_user).order_by('-id')
    return render(request, 'mypass.html', {"user": current_user, 'passwords': passwords})

@login_required(login_url='/')
def passgen(request):
    current_user = User.objects.get(username=request.user)
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST.get('confirm_password', '')

        if confirm_password:
            if confirm_password != password:
                messages.error(request, "Password and confrim password missed matched!!")
                return redirect('/dashboard')
            else:
                new_password = MyPasswords.objects.create(
                    user=current_user,
                    pass_word=password
                )
                new_password.save()
                messages.success(request, "Password is saved successfully..")
                return redirect('/dashboard')
        else:
            new_password = MyPasswords.objects.create(
                user=current_user,
                pass_word=password
            )
            new_password.save()
            messages.success(request, "Password is saved successfully..")
            return redirect('/passgen')
    return render(request, 'passgen.html', {"user": current_user})

@login_required(login_url='/')
def profile(request):
    current_user = User.objects.get(username=request.user)
    return render(request, 'profile.html', {"user": current_user})

