from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,HttpResponseRedirect
from ps4.forms import plusForm,liabilityForm,Nameform,ProductServicesForm, buysnackForm, spendForm, sellstockForm,incomeForm
from django.views import View
from django.views.generic import TemplateView
from ps4.models import ProductsandServices, Transactions
from django.contrib.auth.models import User
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

 
class testView(TemplateView):
	template_name = 'ps4/test.html'
	def get(self,request ):
		form = ProductServicesForm()
		post = ProductsandServices.objects.all() 
		transactions = Transactions.objects.all()
		print(post)

		args = {'form':form, 'post':post}
		return render(request, self.template_name, args)

class incomeView(TemplateView):
	template_name='forms/incomeForm.html'

	def get(self, request):
		form = incomeForm()
		return render(request, self.template_name,{'form':incomeForm()})

	def post(self, request):
		if request.method =='POST':
			form =incomeForm(request.POST)

			if form.is_valid():
				 
				unit_price = form.cleaned_data['unit_price']	
				 
				print(name, description)
				return HttpResponseRedirect('/')

				form =incomeForm()
		args = {'form':form, 'quantity':quantity, 'unit_price':unit_price}
		return render(request, self.template_name, args)


class productserviceView(TemplateView):
	template_name='ps4/productservicesForm.html'

	def get(self, request):
		form = ProductServicesForm()
		return render(request, self.template_name,{'form':ProductServicesForm()})


class buysnackView(TemplateView):
	template_name = 'forms/buysnackForm.html'
	 
	def get(self, request):
		form = buysnackForm()
		return render(request, self.template_name,{'form':buysnackForm()})

class sellstockView(TemplateView):
	template_name = 'forms/sellsnackForm.html'
	 
	def get(self, request):
		form = sellstockForm()
		return render(request, self.template_name,{'form':sellstockForm()})

class spendView(TemplateView):
	template_name = 'forms/spendForm.html'
	 
	def get(self, request):
		form = spendForm()
		return render(request, self.template_name,{'form':spendForm()})

# class productserviceView(TemplateView):

	# def post(self, request):
	# 	if request.method =='POST':
	# 		form =buysnackForm(request.POST)

	# 		if form.is_valid():
				 
	# 			quantity = form.cleaned_data['quantity']
	# 			amount = form.cleaned_data['unit_price']	

	# 			print(name, description)

	# 	args = {'form':form, 'quantity':quantity, 'unit_price':unit_price}
	# 	return render(request, self.template_name,args)
	

#================================================================================
	# def get(self,request ):
	# 	if request.method =='POST':
	# 		form = Nameform(request.POST)

	# 		if form.is_valid():
	# 			return HttpResponseRedirect('/')

	# 	else:
	# 		form = Nameform()
	# 	return render(request, self.template_name,{'form':form})


	# def get(self, request):
	# 	form = plusForm()
	# 	return render( request, self.template_name, {'form':form})
#================================================================================ 
	# def post(self, request):
	# 	form = plusForm(request.POST)
	# 	if form.is_Valid():
	# 		text = form.cleaned_data['post']

	# 	args = {'form':form, 'text':text}
	# 	return render(request, self.template_name, args)

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
		

		return render(request, self.template_name,{})


#forgot-password template view 
class forgotpasswordView(TemplateView):
	template_name = 'ps4/forgotpassword.html'
	def get(self,request ):
		

		return render(request, self.template_name,{})

#register view 
class registerView(TemplateView):
	template_name = 'ps4/register.html'
	def get(self,request ):
		

		return render(request, self.template_name,{})


