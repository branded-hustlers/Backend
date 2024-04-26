from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__ (self):
        return self.name 
    


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='product_images')
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name