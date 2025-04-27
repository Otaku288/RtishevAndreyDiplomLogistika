from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, CompanyRegistrationForm, UpdateUserForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('product_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CompanyRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему!')
                return redirect('product_list')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('product_list')

def user_update(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance = request.user) 
        if form.is_valid():
            curent_password = form.cleaned_data.get('curent_password')
            if not request.user.check_password(curent_password):
                messages.error(request, "Неверный пароль")
                return redirect('update')
            form.save()
            return redirect('company_orders')
    else:
        form = UpdateUserForm(instance = request.user)
    return render(request, 'accounts/updateuser.html', {'form': form})