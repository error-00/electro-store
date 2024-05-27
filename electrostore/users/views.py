from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from main.models import Category
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth


def login(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))

    context = {"title": "Login", "categories": categories}
    return render(request, "users/login.html", context)


def registration(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    context = {"title": "Sign In", "categories": categories}
    return render(request, "users/registration.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main:index"))
