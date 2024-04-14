from django.db import models


# Create your models here.
class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)

    class Meta:
        db_table = 'categories'
        managed = False

    def __str__ (self):
        return self.name



class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    description = models.TextField(null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    product_review = models.TextField(null=True, default=None)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null = True, default=None)

    class Meta:
        db_table = 'product'
        managed = False

    def __str__ (self):
        return self.product_name
    