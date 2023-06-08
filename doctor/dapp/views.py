from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Doctor, User
# Create your views here.

# User views start


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
                messages.error(request, 'password not valid')
                return redirect('/')
        else:
            messages.error(request, 'Email not valid')
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

# User views end

# Doctor views start


def docsignup(request):
    return render(request, 'docsignup.html')


def doc_signup(request):
    if request.method == "POST":
        name = request.POST['name']
        degree = request.POST['degree']
        contact = request.POST['contact']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        image = request.FILES.get('image')
        category = request.POST['category']
        if Doctor.objects.filter(Email=email).exists():
            messages.error(request, "Email already exist")
            return redirect('/docsignup/')
        elif Doctor.objects.filter(Contact=contact).exists():
            messages.error(request, "Contact already exist")
            return redirect('/docsignup/')
        else:
            Doctor.objects.create(Name=name, Degree=degree, Contact=contact,
                                  Email=email, Password=password, Image=image, Category=category)

            return redirect('/table/')


def table(request):
    res = Doctor.objects.all()
    return render(request, 'table.html', {'res': res})


def delete(request, uid):
    Doctor.objects.filter(id=uid).delete()
    return redirect('/table/')


def update(request, uid):
    res = Doctor.objects.get(id=uid)
    return render(request, 'update.html', {'res': res})


def ureg(request):
    if request.method == "POST":
        hide = request.POST['hide']
        name = request.POST['name']
        degree = request.POST['degree']
        contact = request.POST['contact']
        email = request.POST['email']
        category = request.POST['category']
        Doctor.objects.filter(id=hide).update(Name=name, Degree=degree, Contact=contact,
                                              Email=email, Category=category)
        return redirect('/table/')
