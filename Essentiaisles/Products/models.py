from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Username is required')
        email = self.normalize_email
        user = self.model(username = username, email = email)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    username = models.CharField(max_length = 50, unique = True)
    name = models.CharField(max_length=50, blank = True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number=models.CharField(max_length=13, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()


    def __str__(self):
        return self.username





class Category(models.Model):
    name = models.CharField(max_length = 30, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    



class Product(models.Model):
    name = models.CharField(max_length = 50)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField(blank = True, null=True)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)


    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total = models.FloatField(default = 0.0)

    def __str__(self):
        return f"Cart for {self.user.username}"