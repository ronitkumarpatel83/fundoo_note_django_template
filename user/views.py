from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User


def profile(request):
    first_name = ""
    if request.user.is_authenticated:
        first_name = request.user.first_name
    print(first_name)
    return render(request, 'user/profile.html', {"first_name": first_name})


def index(request):
    return render(request, 'user/index.html')


def registration(request):
    if request.method == "POST":
        print(request.POST)
        user = User.objects.create_user(username=request.POST.get("username"),
                                        password=request.POST.get("password"),
                                        email=request.POST.get("email"),
                                        first_name=request.POST.get("first_name"),
                                        last_name=request.POST.get("last_name"),
                                        phone=request.POST.get("phone"),
                                        location=request.POST.get("location"))

        messages.success(request, "Your account has been successfully created.")

        return redirect('login')

    return render(request, 'user/registration.html')


def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        print(user)
        if user:
            login(request, user)
            messages.success(request, "Successfully log in.")
            return redirect("profile")
    return render(request, 'user/login.html')


def logout(request):
    return render(request, 'user/logout.html')
