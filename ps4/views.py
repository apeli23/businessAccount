from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from ps4.forms import (plusForm, liabilityForm,	Nameform, ProductServicesForm, TransactionsForm,buystockForm, buysodaForm, 
					sellsodaForm, spendForm, sellstockForm, incomeForm, transactionForm,buybiscutForm, sellbiscutForm, 
					buypkForm, sellpkForm, buylolipopForm, selllolipopForm, buyenergydrinkForm,sellenergydrinkForm, buyjuiceForm, selljuiceForm)
from django.views import View
from django.views.generic import TemplateView
from ps4.models import ProductsandServices, Transactions
from django.contrib.auth.models import User
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)


# Create your views here.

# class UploadsView(View):

# 	template_name = 'main/test.html'

# 	def get(self,request ):
# 		if self.request.method =='POST':
# 			form = Nameform(request.POST)

# 			if form.is_valid():
# 				return HttpResponseRedirect('/index/')

# 		else:
# 			form = Nameform()
# 		return render(request, self.template_name,{'form':form})


# class buysnackView(TemplateView):
# 	template_name = 'ps4/test.html'

# 	def get(self,request ):
# 		sform = buysnackForm()
# 		args = {'sform':sform}
# 		return render(request, self.template_name, args)


class psvView(TemplateView):
    template_name = 'records/psv.html'
    def get(self, request):
        form = ProductServicesForm()
        post = ProductsandServices.objects.all()
        args = {'form':form, 'post':post}
        return render(request, self.template_name, args)

class psvupdateView(TemplateView):
	template_name = 'update/psvupdate.html'

	def get(self, request, pk):
		return render(request, self.template_name, {"data": ProductsandServices.objects.get(id=pk)})

	def post(self, request, pk):
		psv = ProductsandServices.objects.get(id=pk)
		form = ProductServicesForm(request.POST)
		psv.name = form.data['name']
		psv.description = form.data['description']
		psv.save()
		return redirect('/productservice/')

class transactionsView(TemplateView):
    template_name = 'records/transactions.html'
    def get(self, request):
        form = TransactionsForm()
        post = Transactions.objects.all()
        args = {'form':form, 'post':post}
        return render(request, self.template_name, args)


class tnsupdateView(TemplateView):
	template_name = 'update/tnsupdate.html'

	def get(self, request, pk):
		
		data = {
			"tns": Transactions.objects.get(id=pk),
			"productservice":ProductsandServices.objects.all(),
			 "transaction_type": [
                ('INC', 'Income'),
                ('EXP', 'Expense'),
                ('LYB', 'Liability'),
            ]
		}
		return render(request, self.template_name,  data)

	def post(self, request, pk):
		tns = Transactions.objects.get(id=pk)
		form = TransactionsForm(request.POST)
		tns.transaction_type = form.data['transaction_type']
		tns.productsandservices = ProductsandServices.objects.get(id=form.data['productsandservices'])
		tns.quantity = form.data['quantity']
		tns.unit_price = form.data['unit_price']		
		tns.customer_name = form.data['customer_name']
		tns.save()
		return redirect('/transactions/'+ str(pk))

class testView(TemplateView):
    template_name = 'ps4/test.html'
    def get(self, request):
        form = ProductServicesForm()
        post = ProductsandServices.objects.all()

        args = {'form':form, 'post':post}
        return render(request, self.template_name, args)
# class buybiscutView(TemplateView):
# 	template_name = 'forms/sellbiskutForm.html'

# 	def get(self, request):
# 		form = buybiscutForm()
# 		return render(request, self.template_name,{'form':buybiscutForm()})

# class transactionsView(TemplateView):
#     template_name = 'records/transactions.html'
#     def get(self,request ):
#         form = transactionForm()
#         transactions = Transactions.objects.all()
#         args={'form':form}
# 		return render(request, self.template_name, args)



class incomeView(TemplateView):
	template_name='forms/incomeForm.html'

	def get(self, request, *args, **kwargs):
		form = incomeForm()
		return render(request, self.template_name,{'form':incomeForm()})

	def post(self, request, *args, **kwargs):
		try:
			income = incomeForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)

# class productserviceView(TemplateView):
# 	template_name='forms/productservicesForm.html'

# 	def get(self, request):
# 		form = ProductServicesForm()
# 		# paginator = Paginator(queryset, 25)

# 		return render(request, self.template_name,{'form':ProductServicesForm()})


class buystockView(TemplateView):
	template_name = 'forms/buysnackForm.html'

	def get(self, request):
		form = buystockForm()
		return render(request, self.template_name,{'form':buystockForm()})

class sellstockView(TemplateView):
	template_name = 'forms/sellsnackForm.html'

	def get(self, request):
		form = sellstockForm()
		return render(request, self.template_name,{'form':sellstockForm()})


# 		SNACKS

# biscut
class buybiscutView(TemplateView):
	template_name = 'forms/sellbiskutForm.html'

	def get(self, request):
		form = buybiscutForm()
		return render(request, self.template_name,{'form':buybiscutForm()})

	def post(self, request, *args, **kwargs):
		try:
			buybiscut = buybiscutForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)

# pk
class sellbiscutView(TemplateView):
	template_name = 'forms/sellbiscutForm.html'

	def get(self, request):
		form = sellbiscutForm()
		return render(request, self.template_name,{'form':sellbiscutForm()})

	def post(self, request, *args, **kwargs):
		try:
			sellsoda = sellbiscutForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)

# biscut
class buybiscutView(TemplateView):
	template_name = 'forms/sellbiscutForm.html'

	def get(self, request):
		form = buybiscutForm()
		return render(request, self.template_name,{'form':buybiscutForm()})

	def post(self, request, *args, **kwargs):
		try:
			buybiscut = buybiscutForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)


class sellbiscutView(TemplateView):
	template_name = 'forms/sellbiscutForm.html'

	def get(self, request):
		form = sellbiscutForm()
		return render(request, self.template_name,{'form':sellbiscutForm()})

	def post(self, request, *args, **kwargs):
		try:
			sellsoda = sellbiscutForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)

# pk
class buypkView(TemplateView):
	template_name = 'forms/sellpkForm.html'

	def get(self, request):
		form = buypkForm()
		return render(request, self.template_name,{'form':buypkForm()})

	def post(self, request, *args, **kwargs):
		try:
			buypk = buypkForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)


class sellpkView(TemplateView):
	template_name = 'forms/sellpkForm.html'

	def get(self, request):
		form = sellpkForm()
		return render(request, self.template_name,{'form':sellpkForm()})

	def post(self, request, *args, **kwargs):
		try:
			sellpk = sellpkForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)

# lollipop
class buylolipopView(TemplateView):
	template_name = 'forms/sellpkForm.html'

	def get(self, request):
		form = buypkForm()
		return render(request, self.template_name,{'form':buypkForm()})

	def post(self, request, *args, **kwargs):
		try:
			buypk = buypkForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)


class selllolipopView(TemplateView):
	template_name = 'forms/selllolipopForm.html'

	def get(self, request):
		form = selllolipopForm()
		return render(request, self.template_name,{'form':selllolipopForm()})

	def post(self, request, *args, **kwargs):
		try:
			selllolipop = selllolipopForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)

class buysodaView(TemplateView):
	template_name = 'forms/sellsodaForm.html'

	def get(self, request):
		form = buysodaForm()
		return render(request, self.template_name,{'form':buysodaForm()})

	def post(self, request, *args, **kwargs):
		try:
			buysoda = buysodaForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)


class sellsodaView(TemplateView):
	template_name = 'forms/sellsodaForm.html'

	def get(self, request):
		form = sellsodaForm()
		return render(request, self.template_name,{'form':sellsodaForm()})

	def post(self, request, *args, **kwargs):
		try:
			sellsoda = sellsodaForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)
 
class buyenergydrinkView(TemplateView):
	template_name = 'forms/buyenergydrinkForm.html'

	def get(self, request):
		form = buyenergydrinkForm()
		return render(request, self.template_name,{'form':buyenergydrinkForm()})

	def post(self, request, *args, **kwargs):
		try:
			buysoda = buyenergydrinkForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)

class sellenergydrinkView(TemplateView):
	template_name = 'forms/sellenergydrinkForm.html'

	def get(self, request):
		form = sellenergydrinkForm()
		return render(request, self.template_name,{'form':sellenergydrinkForm()})

	def post(self, request, *args, **kwargs):
		try:
			sellenergydrink = sellenergydrinkForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)

class buyjuiceView(TemplateView):
	template_name = 'forms/buyjuiceForm.html'

	def get(self, request):
		form = buyjuiceForm()
		return render(request, self.template_name,{'form':buyjuiceForm()})

	def post(self, request, *args, **kwargs):
		try:
			buysoda = buyjuiceForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)
 

class selljuiceView(TemplateView):
	template_name = 'forms/selljuiceForm.html'

	def get(self, request):
		form = selljuiceForm()
		return render(request, self.template_name,{'form':selljuiceForm()})

	def post(self, request, *args, **kwargs):
		try:
			sellenergydrink = sellenergydrinkForm(request.POST)
			Transactions.objects.create(
				unit_price=income.data['unit_price'],
			)
			context = {
				"Message": "Success",
				"Success": True
			}
		except Exception as e:
			context = {
				"Message": "Success",
				"Success": False
			
			}

		return render(request, self.template_name,context=context)
 

class spendView(TemplateView):
	template_name = 'forms/spendForm.html'

	def get(self, request):
		form = spendForm()
		return render(request, self.template_name,{'form':spendForm()})

#Dashboard/index template view
class indexView(TemplateView):
	template_name = 'ps4/index.html'
	def get(self,request ):


		return render(request, self.template_name,{})

		#Playstation template view
class playstationView(TemplateView):
	template_name = 'ps4/Playstation.html'
	def get(self,request ):


		return render(request, self.template_name,{})

#Snacks template view
class snacksView(TemplateView):
	template_name = 'ps4/snacks.html'
	def get(self,request ):


		return render(request, self.template_name,{})


#Drinks template view
class drinksView(TemplateView):
	template_name = 'ps4/drinks.html'
	def get(self,request ):

		return render(request, self.template_name,{})

#Charts template view
class chartsView(TemplateView):
	template_name = 'ps4/charts.html'
	def get(self,request ):


		return render(request, self.template_name,{})


#Records template view
class recordsView(TemplateView):
	template_name = 'ps4/records.html'
	def get(self,request ):


		return render(request, self.template_name,{})


#login template view
class loginView(TemplateView):
	template_name = 'ps4/login.html'
	def get(self,request ):

		return render(request, self.template_name, {})


#forgot-password template view
class forgotpasswordView(TemplateView):
	template_name = 'ps4/forgotpassword.html'
	def get(self, request ):

		return render(request, self.template_name, {})

#register view
class registerView(TemplateView):
    template_name = 'ps4/register.html'
    def get(self,request ):


        return render(request, self.template_name, {})


class productserviceDeleteView(View):


    def get(self, request, pk):
        ProductsandServices.objects.get(id=pk).delete()
        return redirect('/productservice/')

# class productserviceUpdateView(View):
# 	template_name = 'update/updateproductservice.html'

# 	def get(self, request, pk):
#     	psv=ProductsandServices.objects.get(id=pk)
#     	transaction=Transactions.objects.all()
# 	   	args = {'psv':psv, 'transaction':transaction}
#     	return render(request, self.template_name, args)

# class productserviceUpdateView(View):
# 	template_name ='update/updateproductservice.html'

# 	def get(self,request ):
# 		form = ProductServicesForm()
# 		psv= ProductsandServices.objects.all()

#       	args = {'form':form, 'psv':psv}

# 	return render(request, self.template_name,args)


    # def get(self, request):
#        psv= ProductsandServices.objects.all()
#        form = ProductServicesForm()
#        args = {'form':form, 'psv':psv}

   	# return render(render,self.template_name ,{})

	# def get(self,request, pk):

	# 	psv = ProductsandServices.objects.all()
	# 	form = ProductServicesForm()
		# transactions = Transactions.objects.all()
		# print(post)

		# args = {'form':form, 'psv':psv}
		# return render(request,'/update/updateproductservice.html/', args )

	# def post(self, request):
	# 	psv = ProductServicesForm(request.POST)

	# 	if psv.is_valid():

	# 		name =  ProductsandServices.cleaned_data["name"]
	# 		description =  ProductsandServices.cleaned_data["description"]
	# 		psv.save()
			# psv = ProductServicesForm()
			# return redirect('/productservice/')
	# 	try:
	# 		income = incomeForm(request.POST)
	# 		Transactions.objects.create(
	# 			unit_price = unit_price.data["unit_price"])
		# args = {"form":form, "psv":psv}
		# return render(request, self.template_name )

