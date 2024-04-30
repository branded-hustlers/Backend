from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer, User, Roles

class SignUpForm(UserCreationForm):
    other_names = forms.CharField(max_length=60, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    address = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(max_length=255, required=True)
    mobile_phone = forms.CharField(max_length=15, required=True)
    date_of_birth = forms.DateField(required=True)

    class Meta:
        model = Customer
        fields = ['other_names', 'last_name', 'address', 'email', 'mobile_phone', 'username', 'date_of_birth']






class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Customer
        fields = ['username', 'password']




class Staff(UserCreationForm):
    other_names = forms.CharField(max_length=60, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(verbose_name = 'email address', unique=True)
    role = forms.CharField(max_length=20, choices = [(roles.name, roles.value) for roles in Roles])
    mobile_phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['other_names', 'last_name', 'email', 'role' 'mobile_phone', 'username']



class StaffSignIn(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'password']
