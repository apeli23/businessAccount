from django import forms
from .models import Transactions,ProductsandServices

# class testForm(forms.Form):
# 	# amount = forms.IntegerField()
# 	post = forms.CharField()

class plusForm(forms.Form):
	# amount = forms.IntegerField()
	 
	model = Transactions
	fields = ('unit_price','quantity',)

class incomeForm(forms.ModelForm):
	unit_price = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
	# 		'placeholder': 'Quantity'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('unit_price',)

# snacks form
class buysnackForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Quantity'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity',)

class sellstockForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Enter Quantity of pieces sold'
			 
		}))
	class Meta:
		model = Transactions
		fields = ('quantity', )
# drinks form
class buystockForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Quantity'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity',)

class Nameform( forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget =forms.Textarea)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)

class ProductServicesForm(forms.ModelForm):

	name = forms.CharField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'State the product or service'
		}))
	description = forms.CharField( widget=forms.Textarea(
		attrs={
			'class':'form-control',
			'placeholder': 'describe product or service'
		}))
	class Meta:
		model = ProductsandServices
		fields = ('name', 'description',)
class spendForm(forms.ModelForm):

	unit_price = forms.DecimalField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Enter expenditure amount'
		}))
	description = forms.CharField( widget=forms.Textarea(
		attrs={
			'class':'form-control',
			'placeholder': 'State reason'
		}))
	 
	 
	class Meta:
		model = Transactions
		fields = ('unit_price', 'description','transaction_type',)

class liabilityForm(forms.ModelForm):
	class Meta:
		model = Transactions
		fields = ('unit_price', 'customer_name',)


# class Transaction(forms.ModelForm):
# 	class Meta:
# 		model = ProductsandServices
# 		fields = ('productsandservices', 'description',)