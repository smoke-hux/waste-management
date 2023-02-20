from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User

def home(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'home.html', {'error': 'Invalid username or password'})

    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        # Handle registration form submission
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create(username=username, password=password, email=email)

        # TODO: Send email verification to user

        return render(request, 'register.html', {'success': 'Registration successful. Please check your email to verify your account.'})

    return render(request, 'register.html')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required # this is only to ensure that only authenticated users can acces the page.it retrives the username of the currentrly logge in user from the 'request' object and passes it to the 'profile.html' 
def profile(request):
    username = request.user.username
    return render(request, 'profile.html', {'username': username})