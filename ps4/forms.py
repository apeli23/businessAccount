from django import forms
from .models import Transactions,ProductsandServices

# class testForm(forms.Form):
# 	# amount = forms.IntegerField()
# 	post = forms.CharField()

class plusForm(forms.Form):
	# amount = forms.IntegerField()
	 
	model = Transactions
	fields = ('unit_price','quantity',)

class AddForm(forms.ModelForm):
	class Meta:
		model = Transactions
		fields = ('unit_price','quantity',)

class Nameform( forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget =forms.Textarea)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)

class ProductServicesForm(forms.ModelForm):
	class Meta:
		model = ProductsandServices
		fields = ('name', 'description',)

class buysnackForm(forms.ModelForm):
	class Meta:
		model = Transactions
		fields = ('unit_price', 'customer_name',)
# class Transaction(forms.ModelForm):
# 	class Meta:
# 		model = ProductsandServices
# 		fields = ('productsandservices', 'description',)