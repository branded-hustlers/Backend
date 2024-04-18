from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

#Create your models here
class CustomerManager(BaseUserManager):
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
        user.is_admin = True
        user.save(using=self._db)
        return user

class Customer(AbstractBaseUser):
    customer_id = models.AutoField(primary_key=True)
    other_names = models.CharField(max_length=60, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    mobile_phone = models.CharField(max_length=15, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=30, blank=False, null=False, unique=True)
    date_of_birth = models.DateField(blank=False, null=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomerManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'other_names', 'last_name', 'date_of_birth', 'mobile_phone']

    def __str__(self):
        return f"{self.other_names} {self.last_name}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin