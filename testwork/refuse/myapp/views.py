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

@login_required
def profile(request):
    username = request.user.username
    return render(request, 'profile.html', {'username': username})
from django.shortcuts import render
from .models import User

def user_info(request):
    # Get the logged-in user's information
    user = User.objects.get(username=request.user.username)

    # Pass the user's information to the template
    context = {
        'username': user.username,
        'cash_earned': user.cash_earned,
        'organic_garbage_collected': user.organic_garbage_collected,
        'inorganic_garbage_collected': user.inorganic_garbage_collected,
    }
    return render(request, 'user_info.html', context)
