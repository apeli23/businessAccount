"""bps4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from ps4.views import (indexView, testView, tnsView, psvView, psvlistView, tnslistView, transactionsView, psvupdateView, tnsupdateView, playstationView, snacksView, drinksView, 
                       chartsView, buybiscutView, sellbiscutView, buypkView, sellpkView, buylolipopView,selllolipopView, buystockView, sellstockView, buysodaView, sellsodaView, recordsView, loginView,
                       forgotpasswordView, productserviceDeleteView, transactionsDeleteView, buyenergydrinkView, sellenergydrinkView, buyjuiceView, selljuiceView, registerView,
                       spendView, incomeView,playstationrecordsView, savingsView,savingslistView,savingseditView,incomelistView, expenselistView)

app_name = 'ps4'
urlpatterns = [

    url(r'^$', indexView.as_view(), name="index"),
    url(r'^tests/$', testView.as_view(), name="tests"),
    # path('index/',views.index, name='index'),
    url(r'^playstation/$', playstationView.as_view(), name="playstation"),
    url(r'^snacks/$', snacksView.as_view(), name="snacks"),
    url(r'^drinks/$', drinksView.as_view(), name="drinks"),
    url(r'^buybiscut/$', buybiscutView.as_view(), name="buybiscut"),
    url(r'^sellbiscut/$', sellbiscutView.as_view(), name="sellbiscut"),
    url(r'^buypk/$', buypkView.as_view(), name="buypk"),
    url(r'^sellpk/$', sellpkView.as_view(), name="sellpk"),
    url(r'^buylolipop/$', buylolipopView.as_view(), name="buylolipop"),
    url(r'^selllolipop/$', selllolipopView.as_view(), name="selllolipop"),
    url(r'^buysoda/$', buysodaView.as_view(), name="buysoda"),
    url(r'^sellsoda/$', sellsodaView.as_view(), name="sellsoda"),
    url(r'^buyenergydrink/$', buyenergydrinkView.as_view(), name="buyenergydrink"),
    url(r'^sellenergydrink/$', sellenergydrinkView.as_view(), name="sellenergydrink"),
    url(r'^buyjuice/$', buyjuiceView.as_view(), name="buyjuice"),
    url(r'^selljuice/$', selljuiceView.as_view(), name="selljuice"),
    url(r'^charts/$', chartsView.as_view(), name="charts"),
    url(r'^records/$', recordsView.as_view(), name="records"),
    url(r'^login/$', loginView.as_view(), name="login"),
    url(r'^forgotpassword/$', forgotpasswordView.as_view(), name="forgotpassword"),
    url(r'^register/$', registerView.as_view(), name="register"),
    url(r'^buystock/$', buystockView.as_view(), name="buystock"),
    url(r'^productservicelist/$', psvlistView.as_view(), name="productservicelist"),
    url(r'^transactionslist/$', tnslistView.as_view(), name="transactionslist"),
    url(r'^spend/$', spendView.as_view(), name="spendForm"),
    url(r'^sellstock/$', sellstockView.as_view(), name="sellstockForm"),
    url(r'^income/$', incomeView.as_view(), name="incomeForm"),
    url(r'^transactions/$', transactionsView.as_view(), name="transactions"),
    # url(r'^transactionform/$', psvView.as_view(), name="productserviceform"),
    url(r'^productservice/$', psvView.as_view(), name="productservices"),
    url(r'^productservice/delete/(?P<pk>[0-9]+)$', productserviceDeleteView.as_view(),name="deleteProductsandServices"),
    url(r'^productservice/edit/(?P<pk>[0-9]+)$',psvupdateView.as_view(),
         name="editproductservice"),
    url(r'^transactions/edit/(?P<pk>[0-9]+)$',tnsupdateView.as_view(), name="edittransaction"),
    url(r'^transactions/delete/(?P<pk>[0-9]+)$', transactionsDeleteView.as_view(),name="deleteTransactions"),
    url(r'^playstationrecords/$', playstationrecordsView.as_view(), name="playstationrecords"),
    url(r'^savings/$', savingsView.as_view(), name="savings"),
    url(r'^savingslist/$', savingslistView.as_view(), name="savingslist"),
    url(r'^savings/edit/(?P<pk>[0-9]+)$',savingseditView.as_view(), name="editsavings"),
    url(r'^incomelist/$', incomelistView.as_view(), name="incomelist"),
    url(r'^expenselist/$', expenselistView.as_view(), name="expenselist"),
]
 