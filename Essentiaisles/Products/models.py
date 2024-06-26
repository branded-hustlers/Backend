from django.db import models
from Customer.models import Customer
from django.utils.text import slugify

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

    """This function takes a category name and converts it into a slug"""
    def generate_product_id(category_name):

        """Generate a unique product ID based on a category name"""

        category_slug = slugify(category_name)
        product_id = f"product-{category_slug}"
        return product_id
    



class ProductReview(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()



class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    current_stock = models.PositiveIntegerField()
    minimum_stock = models.PositiveIntegerField()
    maximum_stock = models.PositiveIntegerField()
    reorder_quantity = models.PositiveIntegerField()
    storage_location = models.CharField(max_length = 30)
    shelf_life = models.DateTimeField()
    last_update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return  f"{self.product} - {self.shelf_life}"

    def update_product_amount(self):
        self.product.amount = self.current_stock
        self.product.save()