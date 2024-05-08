from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
             messages.info(request,'invalid credentials')
             return redirect('login')
    return render(request,'login.html')
# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('regapp:register')  # Use app_name:URL_name
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('regapp:register')  # Use app_name:URL_name
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                messages.success(request, "You have successfully registered. Please log in.")
                return redirect('regapp:login')  # Use app_name:URL_name
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')