from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import HodSignupForm, PrincipalSignupForm, StudentSignupForm, StaffSignupForm
from .models import CustomUser

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.role == 'hod':
                        return redirect('hod_dashboard')
                    elif user.role == 'principal':
                        return redirect('principal_dashboard')
                    elif user.role == 'student':
                        return redirect('student_dashboard')
                    elif user.role == 'staff':
                        return redirect('staff_dashboard')
                else:
                    messages.error(request, 'Your account is inactive.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def hod_signup(request):
    if request.method == 'POST':
        form = HodSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully signed up as an HOD!')
            return redirect('hod_dashboard')
    else:
        form = HodSignupForm()
    return render(request, 'auth/hod_signup.html', {'form': form})


def principal_signup(request):
    if request.method == 'POST':
        form = PrincipalSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully signed up as a Principal!')
            return redirect('principal_dashboard')
    else:
        form = PrincipalSignupForm()
    return render(request, 'auth/principal_signup.html', {'form': form})


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully signed up as a student!')
            return redirect('student_dashboard')
    else:
        form = StudentSignupForm()
    return render(request, 'auth/student_signup.html', {'form': form})


def staff_signup(request):
    if request.method == 'POST':
        form = StaffSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully signed up as staff!')
            return redirect('staff_dashboard')
    else:
        form = StaffSignupForm()
    return render(request, 'auth/staff_signup.html', {'form': form})


def hod_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'hod':
        return redirect('login')
    return render(request, 'dash/hod_dashboard.html')


def principal_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'principal':
        return redirect('login')
    return render(request, 'dash/principal_dashboard.html')


def student_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'student':
        return redirect('login')
    return render(request, 'dash/student_dashboard.html')


def staff_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'staff':
        return redirect('login')
    return render(request, 'dash/staff_dashboard.html')


def home(request):
    return render(request, 'home/index.html')


def auth(request):
    return render(request, 'home/auth.html' )