from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from ps4.forms import (plusForm, liabilityForm,	Nameform, ProductServicesForm, TransactionsForm,buystockForm, buysodaForm, 
					sellsodaForm, spendForm, sellstockForm, incomeForm, buybiscutForm, sellbiscutForm, 
					buypkForm, sellpkForm, buylolipopForm, selllolipopForm, buyenergydrinkForm,sellenergydrinkForm, buyjuiceForm, selljuiceForm,savingsForm)
from django.views import View
from django.views.generic import TemplateView
from ps4.models import ProductsandServices, Transactions, Savings
from django.contrib.auth.models import User
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from .filters import TransactionsFilter, SavingsFilter


# Create your views here.

class psvView(TemplateView):
    template_name = 'forms/productservicesForm.html'
    def get(self, request, *args, **kwargs):
         
        return render(request, self.template_name, {'form': ProductServicesForm()})

    def post(self, request, *args, **kwargs):
        try:
            psv = ProductServicesForm(request.POST)
            ProductsandServices.objects.create(
                name=psv.data['name'],
                description=psv.data['description'],
            )
            context = {
                "Message": "Success",
                "Success": True
            }
            
        except Exception as e:
            context = {
                "Message": str(e),
                "Success": False
            }

        # this should re
        return redirect('/productservicelist/')


class psvlistView(TemplateView):
    template_name = 'records/psvlist.html'
    def get(self, request):
        form = ProductServicesForm()
        post = ProductsandServices.objects.all()
        args = {'form':form, 'post':post}
        return render( request, self.template_name, args)


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
		return redirect('/productservicelist/')

class transactionsView(TemplateView):
    template_name = 'forms/tnsform.html' 

    def get(self, request, *args, **kwargs):
         
        return render(request, self.template_name, {'form': TransactionsForm()})
    def post(self, request, *args, **kwargs):
        try:
            tns = TransactionsForm(request.POST)
            Transactions.objects.create(
            	transaction_type=tns.data['transaction_type'],
            	productsandservices=ProductsandServices.objects.get(id=tns.data['productsandservices']),
                quantity=tns.data['quantity'],
                unit_price=tns.data['unit_price'],
                customer_name=tns.data['customer_name'],
            )
            context = {
                "Message": "Success",
                "Success": True
            }
            
        except Exception as e:
            context = {
                "Message": str(e),
                "Success": False
            }

        # this should re
        return redirect('/transactionslist/')
class tnslistView(TemplateView):
    template_name = 'records/tnslist.html' 
    
    def get(self, request, *args, **kwargs):
     
        queryset = Transactions.objects.all().order_by('date_created')
        # psv = ProductsandServices.objects.get(id=pk)
        
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page')
       	
       	try:
            tns = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            tns = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            tns = paginator.page(paginator.num_pages)

        myFilter = TransactionsFilter(request.GET, queryset)  
        tns = myFilter.qs
        context = {
        	"title": "tns",
            "data": tns,
            "page": page,
            "myFilter":myFilter ,
        }
        
       

        # context = {'date_created':date_created,'date_updated':date_updated,'transaction_type':transaction_type,'quantity':quantity,'productsandservices':productsandservices,'client':client}

        return render(request, self.template_name , context=context)


class tnsView(TemplateView):
    template_name = 'forms/tnsForm.html'
    def get(self, request, *args, **kwargs):
         
        return render(request, self.template_name, {'form': TransactionsForm()})

    def post(self, request, *args, **kwargs):
        template_name = 'forms/tnsform.html'
        try:
            transaction = TransactionsForm(request.POST)
            # print(school.data)
            Transactions.objects.create(
                transaction_type=transaction.data['transaction_type'],
                quantity=transaction.data['quantity'],
                unit_price=transaction.data['unit_price'],
                productservices=ProductsandServices.objects.get(id=transaction.data['productservices']),
                client_name=transaction.data['client_name'],
            )
            context = {
                'Message': 'Success',
                'Success': True
            }
        except Exception as e:
            context = {
                'Message': str(e),
                'Success': False
            }
        return render(request, self.template_name, context=context)

class tnsupdateView(TemplateView):
	template_name = 'update/tnsupdate.html'

	def get(self, request, pk):
		
		data = {
			"tns": Transactions.objects.get(id=pk),
			"productservice":ProductsandServices.objects.all(),
			 "transaction_type": [		      
				('Income', 'income'),
				('Expense','expense'),
				('Savings', 'savings'),
            ]
		}
		return render(request, self.template_name,  context=data)

	def post(self, request, pk):
		form = TransactionsForm(request.POST)
		tns = Transactions.objects.get(id=pk)
		tns.transaction_type = form.data['transaction_type']
		# print(form.data)
		tns.productsandservices = ProductsandServices.objects.get(id=form.data['productsandservices'])
		tns.quantity = form.data['quantity']
		tns.unit_price = form.data['unit_price']		
		tns.customer_name = form.data['customer_name']
		
		tns.save()
		return redirect('/transactionslist/')

	# def post(self, request, pk):
	# 	tns = Transactions.objects.get(id=pk)
	# 	form = TransactionsForm(request.POST)
	# 	psv.name = form.data['name']
	# 	psv.description = form.data['description']
	# 	psv.save()
	# 	return redirect('/transactionslist/')

class testView(TemplateView):
    template_name = 'ps4/test.html'
    def get(self, request):
        form = ProductServicesForm()
        post = ProductsandServices.objects.all()

        args = {'form':form, 'post':post}
        return render(request, self.template_name, args)

class transactionsDeleteView(View): 

    def get(self, request, pk):
        Transactions.objects.get(id=pk).delete()
        return redirect('/transactionslist/')
 	


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
        return redirect('/productservicelist/')
 
class playstationrecordsView(TemplateView):
    template_name = 'records/playstationrecords.html'
    def get(self, request):
        form = ProductServicesForm()
        post = ProductsandServices.objects.all()
        args = {'form':form, 'post':post}
        return render( request, self.template_name, args)


class savingsView(TemplateView):
	template_name = 'forms/savingsForm.html'

	def get(self, request):
		 
		return render(request, self.template_name,{'form':savingsForm()})	
 	
	def post(self, request, *args, **kwargs):
		template_name = 'forms/tnsform.html'
		try:
			savings = savingsForm(request.POST)
			# print(school.data)
			Savings.objects.create(
                 
			amount=savings.data['amount'],
			expense=savings.data['expense'],
			)
			context = {
			'Message': 'Success',
			'Success': True
			}
		except Exception as e:
			context = {
				'Message': str(e),
				'Success': False
			} 
		return redirect('/transactionslist/')

class savingslistView(TemplateView):
    template_name = 'records/savingslist.html' 
    
    def get(self, request, *args, **kwargs):
     
        queryset = Savings.objects.all() 
        # psv = ProductsandServices.objects.get(id=pk)
        
        paginator = Paginator(queryset, 5)
        page = request.GET.get('page')
       	
       	try:
            svn = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            svn = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            svn = paginator.page(paginator.num_pages)

        myFilter = SavingsFilter(request.GET, queryset)  
        svn = myFilter.qs
        context = {
        	"title": "svn",
            "data": svn,
            "page": page,
            "myFilter":myFilter ,
        }
        
       

        # context = {'date_created':date_created,'date_updated':date_updated,'transaction_type':transaction_type,'quantity':quantity,'productsandservices':productsandservices,'client':client}

        return render(request, self.template_name , context=context)

class savingseditView(TemplateView):
	template_name = 'update/savingsupdate.html'

	def get(self, request, pk):
		return render(request, self.template_name, {"data": Savings.objects.get(id=pk)})

	def post(self, request, pk):
		svg = Savings.objects.get(id=pk)
		form = SavingsForm(request.POST)
		svg.amount = form.data['amount']
		svg.expense = form.data['expense']
		svg.save()
		return redirect('/savingslist/')


class incomelistView(TemplateView):
    template_name = 'records/incomelist.html'
    def get(self, request):
        form = TransactionsForm()
        tns = Transactions.objects.filter(transaction_type='Income')
        args = {form:'form','tns':tns}
        return render( request, self.template_name, args)

class expenselistView(TemplateView):
    template_name = 'records/expenselist.html'
    def get(self, request):
        form = TransactionsForm()
        tns = Transactions.objects.filter(transaction_type='Expense')
        args = {form:'form','tns':tns}
        return render( request, self.template_name, args)