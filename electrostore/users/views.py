from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from main.models import Category
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from carts.models import Cart


def login(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key
            if user:
                auth.login(request, user)

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {"title": "Login", "categories": categories, "form": form}
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

    context = {"title": "Sign In", "categories": categories, "form": form}
    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        "title": f"Profile - {request.user.username}",
        "categories": categories,
        "form": form,
    }
    return render(request, "users/profile.html", context)


@login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main:index"))
