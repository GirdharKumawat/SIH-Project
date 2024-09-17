from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered.")
            else:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password1, first_name=name)
                    user.save()
                    # Automatically log the user in after successful signup
                    user = authenticate(request, username=username, password=password1)
                    if user is not None:
                        login(request, user)  # Logs the user in
                        return redirect('home')  # Redirect to home page
                except ValidationError as e:
                    messages.error(request, f"Error creating account: {e}")
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'signup.html')

@login_required(login_url='userLogin')
def home(request):
    return render(request, 'index.html')  

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

@login_required(login_url='userLogin')
def userLogout(request):
    logout(request)
    messages.success(request,'Logout Successfull.....')
    return redirect('userLogin') 
def candidates(request):
    return render(request,'candidates.html')
