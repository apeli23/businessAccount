from django.shortcuts import get_object_or_404, render
from ps4.models import Task, Accounts
from django.template import RequestContext

# Create your views here.

#check lines 13, 33
def Dashboard(request):
	page_title = 'dashboard'
	context = {'page_title':page_title}
	template = 'index.html'
	
	return render(request,template,context)