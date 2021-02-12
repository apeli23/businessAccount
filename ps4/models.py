from django.db import models
from datetime import datetime

# Create your models here.
class ProductsandServices(models.Model):
	name = models.CharField(max_length=10, blank=False, null=False)
	description = models.TextField(max_length=200)
	
	class Meta:         
		verbose_name = "productsandservice"
		verbose_name_plural = "productsandservices"

	def __str__(self):
		return self.name


class Transactions(models.Model):
	TRANSACTION_TYPES = [
		
		('Income', 'income'),
		('Expense','expense'),
		('Savings', 'savings'),
		 		
		]

	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	# is_liability = models.BooleanField(default=False)
	transaction_type = models.CharField(max_length=10, blank=False, null=False, choices=TRANSACTION_TYPES, default='income')
	quantity = models.DecimalField(decimal_places=2, max_digits=8)
	unit_price = models.IntegerField( default=0 )			
	productsandservices = models.ForeignKey(ProductsandServices, default = 1,on_delete=models.CASCADE)
	# description = models.TextField(max_length=200)
	customer_name = models.CharField(max_length=15, default='client')
 	
	# def __str__(self):
	# 	return "%s transaction_type %s quantity %s unit_price %s productsandservices %s customer_name" % (
	# 		self.transaction_type, self.quantity, self.unit_price, self.productsandservices.name, self.customer_name)

class Savings(models.Model):
	date = models.DateTimeField(auto_now_add=True, null=True)
	# date_updated = models.DateTimeField(auto_now=True)
	amount = models.IntegerField( default=0 )
	expense = models.CharField(max_length=10, default='Null',blank=False)
	  