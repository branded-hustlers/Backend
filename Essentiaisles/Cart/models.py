from django.db import models
from Customer.models import Customer
from Products.models import Product



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


# # Create Order Model
# class Order(models.Model):
# 	# Foreign Key
# 	user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
# 	full_name = models.CharField(max_length=250)
# 	email = models.EmailField(max_length=250)
# 	shipping_address = models.TextField(max_length=15000)
# 	amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
# 	date_ordered = models.DateTimeField(auto_now_add=True)	

# 	def __str__(self):
# 		return f'Order - {str(self.id)}'

# # Create Order Items Model
# class OrderItem(models.Model):
# 	# Foreign Keys
# 	order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
# 	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
# 	user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

# 	quantity = models.PositiveBigIntegerField(default=1)
# 	price = models.DecimalField(max_digits=7, decimal_places=2)


# 	def __str__(self):
# 		return f'Order Item - {str(self.id)}'

##After this then you makemigrations (I mean for the Order and OrderItem)
