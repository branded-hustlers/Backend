from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def success(request):
    return render(request, 'registration/success.html')