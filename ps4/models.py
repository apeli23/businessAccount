from django.db import models
from datetime import datetime

# Create your models here.
class ProductsandServices(models.Model):
	name = models.CharField(max_length=10)
	description = models.TextField(max_length=200)
	
	def __str__(self):
		return self.name


class Transactions(models.Model):
	TRANSACTION_TYPE = (
		
		('Income', 'income'),
		('Expense','expense'),
		('Liability', 'liability'),
		
		)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	transaction_type = models.CharField(max_length=10, blank=False, null=False, choices=TRANSACTION_TYPE,default='Income')
	quantity = models.IntegerField(default=0)
	unit_price = models.DecimalField(decimal_places=2, max_digits=8)
	productsandservices = models.ForeignKey(ProductsandServices, default = 1,on_delete=models.CASCADE)
	description = models.TextField(max_length=200)
	customer_name = models.CharField(max_length=15, default='client')
 	