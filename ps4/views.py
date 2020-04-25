from django.shortcuts import render
from django.http import HttpResponse 
 
# Create your views here.
 
#Dashboard/index template view
def index(request):
	# return HttpResponse("index page view")
	return render(request, 'ps4/index.html')

#Playstation template view
def playstation(request):
	#return HttpResponse("playstation page view")
	return render(request, 'ps4/playstation.html')

#Snacks template view 
def snacks(request):
	# return HttpResponse("snacks page view")
	return render(request, 'ps4/snacks.html')

#Drinks template view 
def drinks(request):
	# return HttpResponse("drinks page view")
	return render(request, 'ps4/drinks.html')

#Charts template view 
def charts(request):
	# return HttpResponse("charts page view")
	return render(request, 'ps4/charts.html')

#Records template view 
def records(request):
	# return HttpResponse("records page view")
	return render(request, 'ps4/records.html')





































	