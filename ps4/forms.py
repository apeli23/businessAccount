from django import forms
from .models import Transactions,ProductsandServices, Savings

# class testForm(forms.Form):
# 	# amount = forms.IntegerField()
# 	post = forms.CharField()


class TransactionsForm(forms.ModelForm):

	TRANSACTION_TYPES = (
		('Income', 'income'),
		('Expense','expense'),
		('Savings', 'savings'),
	)

	transaction_type = forms.ChoiceField(
		choices=TRANSACTION_TYPES,
		required=True,
		label='TRANSACTION TYPE',
		widget=forms.Select(
			attrs={
				'class': 'form-control', 
			}
		)
	)
	
	productsandservices = forms.ModelChoiceField(
		queryset=ProductsandServices.objects.all(),
		label='PRODUCT/SERVICE',
		widget=forms.Select(
			attrs={
				'class': 'form-control',
			}
		
		)
	)
	
	quantity = forms.DecimalField( 
		required=False, 
        widget=forms.TextInput(
			attrs={
			'class':'form-control',
			}
		)
	)

	unit_price = forms.IntegerField( 
		label='AMOUNT',
        required=True,
        widget=forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'ENTER AMOUNT:',
			 
		}))
	customer_name = forms.CharField( widget=forms.TextInput(
		 
		attrs={
			'class':'form-control',
			 
		}))
	 
	class Meta:
		model = Transactions
		fields = '__all__'

class plusForm(forms.Form):
	# amount = forms.IntegerField()
	 
	model = Transactions
	fields = ('unit_price','quantity',)

class incomeForm(forms.ModelForm):
	unit_price = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Income Amount:'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('unit_price',)

class savingsForm(forms.ModelForm):
	
	amount = forms.IntegerField( 
		label='',
        required=True,
        widget=forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'AMOUNT'
					 			 
		}))
	expense = forms.CharField( widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder':'EXPENSE'
			 
		}))

	class Meta:
		model = Savings
		fields = '__all__'

 
class buybiscutForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Product quantity:'
		}))
	unit_price =  forms.DecimalField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'product price:'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity','unit_price',)

class sellbiscutForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'quantity of product sold:'
		}))
	
	class Meta:
		model = Transactions
		fields = ('quantity',)

# pk
class buypkForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Product quantity:'
		}))
	unit_price =  forms.DecimalField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'product price:'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity','unit_price',)

class sellpkForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'quantity of product sold:'
		}))
	
	class Meta:
		model = Transactions
		fields = ('quantity',)

# lolipop
class buylolipopForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Product quantity:'
		}))
	unit_price =  forms.DecimalField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'product price:'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity','unit_price',)

class selllolipopForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'quantity of product sold:'
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

class buysodaForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Product quantity:'
		}))
	unit_price =  forms.DecimalField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'product price:'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity','unit_price',)

class buypkForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Product quantity:'
		}))
	unit_price =  forms.DecimalField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'product price:'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity','unit_price',)

class buylolipopForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Product quantity:'
		}))
	unit_price =  forms.DecimalField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'product price:'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity','unit_price',)
 

class sellsodaForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Bottle quantity sold:'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity',)

class buyenergydrinkForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Bottle quantity received:'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity',)


class sellenergydrinkForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Bottle quantity received:'
		}))
	 
	 
	class Meta:
		model = Transactions
		fields = ('quantity',)

class buyjuiceForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Amount Aquired:'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity',)

 
class selljuiceForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Amount Aquired:'
		}))
	 
	class Meta:
		model = Transactions
		fields = ('quantity',)
		
class buystockForm(forms.ModelForm):
	quantity = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Quantity:'
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
		fields = '__all__'

class spendForm(forms.ModelForm):

	unit_price = forms.DecimalField(required=True, widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder': 'Enter expenditure amount'
		}))
	description = forms.CharField( widget=forms.Textarea(
		attrs={
			'class':'form-control',
			'placeholder': 'State product or service'
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