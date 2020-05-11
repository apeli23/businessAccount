from django.urls import path

from ps4 import views

app_name = 'ps4'
urlpatterns = [
	path('index/',views.index, name='index'),
	path('playstation/',views.playstation, name='playstation'),
	path('snacks/',views.snacks, name='snacks'),
	path('drinks/',views.drinks, name='drinks'),
	path('charts/',views.charts, name='charts'),
	path('records/',views.records, name='records'),
	path('login/',views.login, name='login'),
	path('forgotpassword/',views.forgotpassword, name='forgotpassword'),
	path('register/',views.register, name='register'),
]