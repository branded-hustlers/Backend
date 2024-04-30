from django.urls import path
from .views import SignUpView,CreateUserView, LoginView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('createuser/', CreateUserView.as_view(), name='create user'),
    path('login/', LoginView.as_view(), name='login'),
]