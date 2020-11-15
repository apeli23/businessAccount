import django_filters
from django_filters import DateFilter
from .models import *


class TransactionsFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name = "date_created",lookup_expr='gte')
	end_date = DateFilter(field_name = "date_created",lookup_expr='lte')
	class Meta:
		model = Transactions
		fields = '__all__'
		exclude = ['date_created','date_updated','quantity','unit_price']

class SavingsFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name = "date",lookup_expr='gte')
	end_date = DateFilter(field_name = "date",lookup_expr='lte')
	class Meta:
		model = Savings
		fields = '__all__'
		exclude = ['date','date_updated', 'amount']