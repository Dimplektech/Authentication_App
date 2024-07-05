from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def index(request):  
    """
    Render the index page.
    This view is for pages that do not require authentication.
    """
    return render(request, 'auth_app/index.html')


def register(request):
    """
    Handle User registration using the built-in User model.
    If the request method is POST, it processes the form data and registers
    the user.
    If the form is valid, the user is saved and redirected to the login page
    with a success message.
    If the request method is GET, it displays a blank registration form.
    """
    if request.method == 'POST':
        # Instantiate the form with POST data.
        form = UserRegisterForm(request.POST) 
        if form.is_valid():  # Check if the form is valid.
            form.save()  # Save the form data to create a new user.
            # Get the username from the cleaned data
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')   # Redirect to the login page
    else:
        form = UserRegisterForm()  # Instantiate a blank form for GET request
    # Render the registration page with the form
    return render(request, 'auth_app/register.html', {'form': form})
    

def login_view(request):
    """
    Handled user login using the built-in User model.
    If the request method id POST, It autheticates the user with the provided
    credentials.
    If authetication is successfull, the user is logged in and redirected to 
    the index page.
    if the request method is GET, it  displays a blank login form.
    """
    if request.method == 'POST':
        # Instantiate the form with POST data# Instantiate the form with POST
        # data
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('index')   # Redirect to the index page.
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')    

    form = AuthenticationForm()  # Instantiate a blank form for GET request.
    # Render the login page with the form
    return render(request, 'auth_app/login.html', {'form': form})


def logout_view(request):
    """
    Handle user logout.
    Logs out the user and redirects to the index page with a success message.
    """
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('index')  # Redirect to the index page


def protected_view(request):
    """
    Render a protected page that requires authentication.
    If the user is not authenticated, they are redirected to the login page.
    """
    if not request.user.is_authenticated:
        # Redirect to the login page if not authenticated
        return redirect('login')
    # Render the protected page
    return render(request, 'auth_app/protected.html')
