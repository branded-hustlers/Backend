from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from Customer.models import Customer

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # First, try to authenticate with the built-in User model
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass

        try:
            # If the built-in User model authentication fails, try with the Customer model
            user = Customer.objects.get(username=username)
            if user.check_password(password):
                return user
        except Customer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            try:
                user = Customer.objects.get(pk=user_id)
            except Customer.DoesNotExist:
                return None
        return user