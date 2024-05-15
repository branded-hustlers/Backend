from django.urls import path
from .views import CreateUserView, LoginView

urlpatterns = [
    path('createuser/', CreateUserView.as_view(), name='create user'),
    path('login/', LoginView.as_view(), name='login'),
]