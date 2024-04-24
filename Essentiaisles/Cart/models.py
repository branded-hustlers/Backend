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


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Ready For Pickup', 'Ready For Pickup'),
        ('Cancelled', 'Cancelled'),
    ]
    
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES)

    
    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer}, Status: {self.order_status}"


class OrderedItem(models.Model):
    ordered_items_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tax = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order Item ID: {self.ordered_items_id}, Order: {self.order}, Product: {self.product}, Quantity: {self.quantity}"
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
