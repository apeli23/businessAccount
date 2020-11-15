from django.contrib import admin
from .models import ProductsandServices, Transactions, Savings

# Register your models here.

admin.site.register(ProductsandServices)
admin.site.register(Transactions)
admin.site.register(Savings)