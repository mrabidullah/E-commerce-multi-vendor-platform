from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignupForm, LoginForm
from sellerapp.models import Seller


# -------------------
# SIGNUP
# -------------------
def signup_view(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST,request.FILES)

        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            image=request.FILES.get("image")

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return render(request, "authentication/signup.html", {"form": form})

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # AUTO CREATE SELLER PROFILE
            Seller.objects.create(
                user=user,
                phone="",
                image=image
            )

            messages.success(request, "Account created successfully!")
            return redirect("authentication:login")

        else:
            print(form.errors)  
            messages.error(request, "only allow characters in username ")

    return render(request, "authentication/signup.html", {"form": form})


# -------------------
# LOGIN
# -------------------
def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                
                if Seller.objects.filter(user=user).exists():
                    return redirect("profile")
                else:
                    return redirect("home")

            else:
                messages.error(request, "Invalid credentials")

    return render(request, "authentication/login.html", {"form": form})


# -------------------
# LOGOUT
# -------------------

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("authentication:login")