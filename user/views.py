from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages


def profile(request):
    return render(request, 'user/profile.html')


def registration(request):
    if request.method == "POST":
        user = User.objects.create(username=request.POST.get("username"),
                                   password=request.POST.get("password"),
                                   email=request.POST.get("email"),
                                   first_name=request.POST.get("first_name"),
                                   last_name=request.POST.get("last_name"),
                                   phone=request.POST.get("phone"),
                                   location=request.POST.get("location"))
        user.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('login')

    return render(request, 'user/registration.html')


def login(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            request.user = user
            first_name = user.first_name
            return render(request, "user/profile.html", {"first_name": first_name})
        else:
            messages.error(request, "Bad Credential")
            return redirect('profile')
    return render(request, 'user/login.html')


def logout(request):
    return render(request, 'user/logout.html')
