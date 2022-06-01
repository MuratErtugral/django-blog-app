from django.shortcuts import render, redirect
from django.contrib.auth import logout,login
from .forms import  UserForm,ProfileForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')

def register(request):
    
    form_user = UserForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)

        if form_user.is_valid():
            user = form_user.save()

            login(request, user)
            return redirect ('home')

    context = {
        'form_user' : form_user,
    }

    return render(request, 'users/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'users/login.html', {"form":form})

def profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        student = form.save()
        
        if 'avatar' in request.FILES:
            student.avatar = request.FILES.get('avatar')
            student.save()
        return redirect('home')

    context = {
        'form' : form
    }
    return render(request,'users/profile.html', context)