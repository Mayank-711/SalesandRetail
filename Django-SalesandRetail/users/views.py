from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid
from .models import Profile
from .utils import send_email_to_client
import uuid
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    current_user = request.user
    user_id=current_user.username
    context = {"user_id":user_id}
    return render(request,'inventory/dashboard.html',context=context)

def SignupPage(request):
    try:
        if request.method =='POST':
            username = request.POST.get('username')
            email=request.POST.get('email')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            try:
                if pass1!= pass2:
                    messages.info(request, "Password and Confirm Password are not Same.")
                    return redirect("signup")
                user=User.objects.filter(username=username)
                if user.exists():
                    messages.info(request, "User with same username already exists.")
                    return redirect("signup")
                user=User.objects.filter(email=email)
                if user.exists():
                    messages.info(request, "Email already exists.")
                    return redirect("signup")
                else:
                    my_user = User.objects.create_user(username,email,pass1)
                    my_user.save()
                    messages.info(request, "Account created successfully.please login to continue.")
                profile_obj=Profile.objects.create(user=my_user)
                profile_obj.save()
                return redirect('login')
   
            except Exception as e:
                print(e)  
    except Exception as e:
        print(e)

    return render(request,'users/signup.html')

def LoginPage(request):
    try:    
        if request.method=='POST':
            username=request.POST.get('username')
            pass1=request.POST.get('pass')
            if not User.objects.filter(username=username).exists():
                messages.error(request,'Invalid Username')
                return redirect("login")

            user=authenticate(username=username,password=pass1)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,"Invalid Credentials")
                return redirect("login")
    except Exception as e:
        print(e)
    return render(request,'users/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')





def ChangePassword(request,token):
    context={}
    try:
        profile_obj=Profile.objects.filter(forgot_password_token=token).first()
        print(profile_obj)
        context={"user_id":profile_obj.user.id}

        if request.method=="POST":
            new_password=request.POST.get("newpassword")
            confirm_password=request.POST.get("reconfirmpassword")
            user_id=request.POST.get("user_id")

            if user_id is None:
                messages.success(request,"No User Id Found")
                return redirect(f"/ChangePassword/{token}/")
            
            if new_password!=confirm_password:
                messages.error(request,"Password does not match with above")
                return redirect(f"/ChangePassword/{token}/")
            
            user_obj=User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect("login")


    except Exception as e:
        print(e)
    return render(request,"users/ChangePassword.html",context)

def ForgotPassword(request):
    try:
        if request.method=="POST":
            data=request.POST
            username=data.get("username")
            if not User.objects.filter(username=username).first():
                messages.success(request,"No Username Found with this Username")
                return redirect("ForgotPassword")
            user_obj=User.objects.get(username=username)
            token=str(uuid.uuid4())
            profile_obj=Profile.objects.get(user=user_obj)
            profile_obj.forgot_password_token=token
            profile_obj.save()
            send_email_to_client(user_obj.email,token)
            messages.success(request,"Email has been sent")
            return redirect("ForgotPassword")


    except Exception as e:
        print(e) 
    return render(request,"users/ForgotPassword.html")