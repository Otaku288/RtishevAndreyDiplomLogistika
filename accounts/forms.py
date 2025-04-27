from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import Company

class CompanyRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100, label="Название компании")
    phone_number = forms.CharField(max_length=20, label="Телефон")
    warehouse_address = forms.CharField(widget=forms.Textarea, label="Адрес склада")

    class Meta:
        model = Company
        fields = ['username', 'company_name', 'email', 'phone_number', 'warehouse_address', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'})) 

class UpdateUserForm(UserChangeForm):
    curent_password = forms.CharField()
    class Meta:
        model = Company
        fields = ['email', 'phone_number']
        