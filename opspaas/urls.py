"""devopsWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()
from app01.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',login),
    url(r'^index/$',index),
    url(r'^account_login/$',account_login),
    url(r'^logout/$',logout),
    url(r'^server_manager/$',server_manager),
    url(r'^addserver/$',addserver),
    url(r'^delete$',delete_server,name="delete_server"),
    url(r'^delselect',delselect,name='delselect'),
    url(r'^query',query,name='query')
]
