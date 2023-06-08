from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Doctor, User
# Create your views here.


def userlogin(request):
    return render(request, "userlogin.html")


def login_reg(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(Email=email).exists():
            res = User.objects.get(Email=email)
            psw = res.Password
            if check_password(password, psw):
                return redirect('/table/')
            else:
                messages.error(request, 'Password not valid')
                return redirect('/')
        else:
            messages.error(request, 'Email is not valid')
            return redirect('/')


def usersignup(request):
    return render(request, "usersignup.html")


def user_signup(request):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if User.objects.filter(Email=email).exists():
            messages.error(request, "Email already exist")
            return redirect('/usersignup/')
        elif User.objects.filter(Contact=contact).exists():
            messages.error(request, "Contact already exist")
            return redirect('/usersignup/')
        else:
            User.objects.create(Name=name, Contact=contact,
                                Email=email, Password=password)
            return redirect('/')

    # User View End
