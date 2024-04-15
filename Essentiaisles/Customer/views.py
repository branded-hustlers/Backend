from django.http import JsonResponse
from django.contrib.auth import login
from .models import Customer
from .forms import CustomerForm

def register(request):
  if request.method == 'POST':
    form = CustomerForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data['email']
      password = generate_strong_password()  # Replace with your password generation function
      user = Customer.objects.create_user(email, password)
      login(request, user)
      return JsonResponse({'message': 'User registration successful!'})
  else:
    return JsonResponse({'message': 'Invalid registration data.'})
