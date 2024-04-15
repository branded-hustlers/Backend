from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
       model = Customer


    other_names = forms.CharField(label="Other Names", max_length=60, required=True)
    last_name = forms.CharField(label="Last Name", max_length=30, required=True)
    address = forms.CharField(label="Address", max_length=50)
    email = forms.EmailField(label="Email", required=True)
    mobile_phone = forms.CharField(label="Phone Number", max_length=15, required=True)
    username = forms.CharField(label="Username", max_length=30, required=True)
    date_of_birth = forms.DateField(label="Date of Birth", required=True, input_formats=['%Y-%m-%d'])

    def clean_mail(email):
        email = email.strip().lower()
        email = email.replace('..', '.').replace(' ', '')
        return email

    def save(self, commit=True):
        customer = super().save(commit=False)
        if 'password' in self.cleaned_data:
            from django.contrib.auth.hashers import make_password
            customer.password = make_password(self.cleaned_data['password'])

        if commit:
         customer.save()
         return customer