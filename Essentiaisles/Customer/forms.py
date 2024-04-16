from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer

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