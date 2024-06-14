from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import logout

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            print(form)
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('task_list')  # Redirect to home page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')  # Redirect to home page after successful login
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')  
