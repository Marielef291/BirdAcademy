from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.forms import NewUserForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Identifiant ou mot de passe incorrect")

    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect ("accounts:login")

def register_user(request):
    if request.method=='POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription réussie ! Veuillez vous connecter.")
            return redirect ("accounts:login")
    else :
        form = NewUserForm()
        
    return render (request, "accounts/register.html",{"form": form})
