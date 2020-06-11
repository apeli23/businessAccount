from django.urls import path
from ps4 import views
from ps4.views import (indexView, testView, playstationView, snacksView, drinksView, chartsView, buysnackView, sellstockView
					,recordsView,loginView	,forgotpasswordView	,registerView, productserviceView, spendView, incomeView)
from django.conf.urls import url

app_name = 'ps4'
urlpatterns = [
	url(r'^$', indexView.as_view(), name="index"),
	url(r'^tests/$', testView.as_view(), name="tests"), 
	# path('index/',views.index, name='index'),
	url(r'^playstation/$', playstationView.as_view(), name="playstation"),
	url(r'^snacks/$', snacksView.as_view(), name="snacks"),
	url(r'^drinks/$', drinksView.as_view(), name="drinks"),
	url(r'^charts/$', chartsView.as_view(), name="charts"),
	url(r'^records/$', recordsView.as_view(), name="records"),
	url(r'^login/$',loginView.as_view(), name="login"),
	url(r'^forgotpassword/$',forgotpasswordView.as_view(), name="forgotpassword"),
	url(r'^register/$',registerView.as_view(), name="register"),
	url(r'^buysnack/$', buysnackView.as_view(), name="buysnack"),
	url(r'^productservice/$', productserviceView.as_view(), name="productserviceForm"), 
	url(r'^spend/$', spendView.as_view(), name="spendForm"), 
	url(r'^sellstock/$', sellstockView.as_view(), name="sellstockForm"), 
	url(r'^income/$', incomeView.as_view(), name="incomeForm"), 
]