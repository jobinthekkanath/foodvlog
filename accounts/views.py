from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile  # Adjust this import based on your actual model structure

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid details')
            return redirect('login')
    return render(request, "login.html")

def register(request):
    
    if request.method == "POST":
        print("post")
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user( username=username, password=password1, email=email,
                    first_name=firstname, last_name=lastname,is_active=True
                    
                )
                UserProfile.objects.create(user=user)
                messages.success(request, "User created successfully")
                return redirect('/')
        else:
            messages.error(request, "Passwords did not match")
            return redirect('register')
    else:
        return render(request, 'register.html')


def logout(request):
    auth_logout(request)
    return redirect('/')














# from django.contrib import messages
# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User,auth
# from . models import *
# from .models import UserProfile 


# # Create your views here.
# def login(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,'invalid details')
#             return redirect('login')
#     return render(request,"login.html")
# def register(request):
#     if request.method=="POST":
#         firstname=request.POST['firstname']
#         lastname = request.POST['lastname']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']
#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"username taken")
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,"email taken")
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(username=username,password=password1,email=email,firstname=firstname,lastname=lastname)
#                 user.save();
#                 UserProfile.objects.create(user=user)
#               messages.success(request, "User created successfully")
#               return redirect('/')
#         else:
#             print("password didnot matched")
#             return redirect('register')
#         return redirect('/')
#     else:
#         return  render(request,'register.html')
# def logout(request):
#     auth.logout(request)
#     return redirect('/')

