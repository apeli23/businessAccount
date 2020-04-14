"""bps2 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin  
 
from ps4 import views as ps4_views
from bps2 import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),  
    # url(r'^', include('catalog.urls')), 

    url(r'^', include('ps4.urls', namespace="ps4")),
     
]