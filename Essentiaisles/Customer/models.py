# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models
# from enum import Enum

# #Create your models here

# class Roles(Enum):
#     CLERK = 'Clerk'
#     DELIVERY = 'Delivery'
#     ADMIN = 'Admin'


# class CustomerManager(BaseUserManager):
#     def create_user(self, email, username, other_names, last_name, date_of_birth, mobile_phone, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             other_names=other_names,
#             last_name=last_name,
#             date_of_birth=date_of_birth,
#             mobile_phone=mobile_phone,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, other_names, last_name, date_of_birth, mobile_phone, password):
#         user = self.create_user(
#             email=email,
#             username=username,
#             other_names=other_names,
#             last_name=last_name,
#             date_of_birth=date_of_birth,
#             mobile_phone=mobile_phone,
#             password=password,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.save(using=self._db)
#         return user
    

# class User(AbstractBaseUser):
#     other_names = models.CharField(max_length=60, blank=False, null=False)
#     last_name = models.CharField(max_length = 30, blank=False, null=False)
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     date_of_birth = models.DateField(blank=False, null=False)
#     mobile_phone = models.CharField(max_length=15, blank=False, null=False, unique=True)
#     password = models.CharField(max_length = 255, blank = False, null = False)
#     username = models.CharField(max_length = 30, blank=False, null=False, unique=True)
#     role = models.CharField(max_length=20, choices=[(roles.name, roles.value) for roles in Roles])

#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=True)
    
#     objects = CustomerManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'other_names', 'last_name', 'date_of_birth', 'mobile_phone']

#     def __str__(self):
#         return f"{self.other_names} {self.last_name}"








# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     address = models.CharField(max_length=50, blank=True, null=True)
#     # other_names = models.CharField(max_length=60, blank=False, null=False)
#     # last_name = models.CharField(max_length=30, blank=False, null=False)
#     # address = models.CharField(max_length=50, blank=True, null=True)
#     # email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     # mobile_phone = models.CharField(max_length=15, blank=False, null=False, unique=True)
#     # password = models.CharField(max_length=255, blank=False, null=False)
#     # username = models.CharField(max_length=30, blank=False, null=False, unique=True)
#     # date_of_birth = models.DateField(blank=False, null=False)

#     # is_active = models.BooleanField(default=True)
#     # is_admin = models.BooleanField(default=False)

#     # objects = CustomerManager()

#     # USERNAME_FIELD = 'username'
#     # REQUIRED_FIELDS = ['email', 'other_names', 'last_name', 'date_of_birth', 'mobile_phone']

#     def __str__(self):
#         return f"{self.other_names} {self.last_name}"
    







    

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from enum import Enum

class Roles(Enum):
    CLERK = 'Clerk'
    DELIVERY = 'Delivery'
    ADMIN = 'Admin'
    CUSTOMER = 'Customer'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, other_names, last_name, date_of_birth, mobile_phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            other_names=other_names,
            last_name=last_name,
            date_of_birth=date_of_birth,
            mobile_phone=mobile_phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, other_names, last_name, date_of_birth, mobile_phone, password):
        user = self.create_user(
            email=email,
            username=username,
            other_names=other_names,
            last_name=last_name,
            date_of_birth=date_of_birth,
            mobile_phone=mobile_phone,
            password=password,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.role = Roles.ADMIN
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    other_names = models.CharField(max_length=60, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    mobile_phone = models.CharField(max_length=15, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=30, blank=False, null=False, unique=True)
    role = models.CharField(max_length=20, choices=[(roles.name, roles.value) for roles in Roles], default=Roles.CUSTOMER)
    date_of_birth = models.DateField(blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'other_names', 'last_name', 'date_of_birth', 'mobile_phone']

    def __str__(self):
        return f"{self.other_names} {self.last_name}"

    def save(self, *args, **kwargs):
        if self.role != Roles.CUSTOMER.value:
            self.is_staff = True
        else:
            self.is_staff = False
        super().save(*args, **kwargs)


    def has_module_perms(self, app_label):
        """
        Returns True if the user has permissions to access the specified app.
        """
        if self.is_admin:
            return True
        if self.is_staff:
            return self.user_permissions.filter(codename__startswith=f'view_{app_label}').exists()
        return False
