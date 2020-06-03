from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,HttpResponseRedirect
from ps4.forms import plusForm,AddForm,Nameform,ProductServicesForm, buysnackForm
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


class buysnackView(TemplateView):
	template_name = 'ps4/test.html'

	def get(self,request ):
		sform = buysnackForm()
		return render(request, self.template_name, {'sform':sform})

 
class testView(TemplateView):
	template_name = 'ps4/test.html'
	def get(self,request ):
		form = ProductServicesForm()
		post = ProductsandServices.objects.all().order_by( '-date_created') 
		transactions = Transactions.objects.all()
		# print(post)

		form = ProductServicesForm()
		post = ProductsandServices.objects.all() 
		args = {'form':form, 'post':post}
		return render(request, self.template_name, args)
	# template_name = 'ps4/test.html'

	# def get(self, request):
	# 	form = AddForm()
	# 	return render(request, self.template_name,{'form':form})

	# def post(self, request):
	# 	if request.method =='POST':
	# 		form =AddForm(request.POST)

	# 		if form.is_valid():
				 
	# 			name = form.cleaned_data['name']
	# 			description = form.cleaned_data['description']	

	# 			print(name, description)

	# 	args = {'form':form, 'name':name, 'desctiption':description}
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
