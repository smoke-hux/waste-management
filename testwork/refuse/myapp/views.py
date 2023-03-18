from django.shortcuts import render

# Create your views here.
# takes a request and returns a response

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
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

def user_info(request):
    # Get the logged-in user's information
    user = User_info.objects.get(username=request.user.username)

    # Pass the user's information to the template
    context = {
        'username': user.username,
        'cash_earned': user.cash_earned,
        'organic_garbage_collected': user.organic_garbage_collected,
        'inorganic_garbage_collected': user.inorganic_garbage_collected,
    }
    return render(request, 'user_info.html', context)
def register(request):
    if request.method == 'POST':
        # Handle registration form submission
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()

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
from .models import User_info

def user_info(request):
    # Get the logged-in user's information
    user = User_info.objects.get(username=request.user.username)

    # Pass the user's information to the template
    context = {
        'username': user.username,
        'cash_earned': user.cash_earned,
        'organic_garbage_collected': user.organic_garbage_collected,
        'inorganic_garbage_collected': user.inorganic_garbage_collected,
    }
    return render(request, 'user_info.html', context)
def admin_info(request):
    if request.method == 'POST':
        # get the form data
        organic_garbage_collected = request.POST.get('organic_garbage_collected')
        inorganic_garbage_collected = request.POST.get('inorganic_garbage_collected')

        # update the garbage collected data in the database
        user = User.objects.get(username='admin')
        user.organic_garbage_collected += float(organic_garbage_collected)
        user.inorganic_garbage_collected += float(inorganic_garbage_collected)
        user.save()

    return render(request, 'admin.html')
