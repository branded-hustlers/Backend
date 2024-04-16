from django.db import models
from Customer.models import Customer
from Products.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Product, through='CartItem')


    def __str__(self):
        return f"Cart for {self.user.username}"
    

    def total_cost(self):
        total = sum(item.product.price * item.quantity for item in self.cartitem_set.all())
        return total
    


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.product.product_name} ({self.quantity} items) in cart for {self.cart.user.username}"



