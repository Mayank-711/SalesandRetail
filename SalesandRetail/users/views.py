from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    current_user = request.user
    user_id=current_user.username
    context = {"user_id":user_id}
    return render(request,'inventory/dashboard.html',context=context)

def SignupPage(request):
    if request.method =='POST':
        uname = request.POST.get('username')
        email=request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password1')
        if pass1 != pass2:
            return HttpResponse("Your Password and Confirm Password are not same")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
        return redirect('login')

    return render(request,'users/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request,'users/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
