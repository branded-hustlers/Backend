from django.urls import path
from .views import SignUpView, LoginView


urlpatterns = [
    path('createuser/', SignUpView.as_view(), name='create user'),
    path('login/', LoginView.as_view(), name='login'),
]