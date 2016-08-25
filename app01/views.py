#coding:utf-8
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth


# Create your views here.
#登录页
def login(request):
	return render_to_response('login.html')
#首页
def index(request):
        return render_to_response('index.html')

#用户登录
def account_login(request):
	print request.POST
	username=request.POST.get('username')
	password=request.POST.get('password')
	user=auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/index/')
	else:
		return render_to_response('login.html',{'login_err':'用户名或密码错误'})

#用户注销
def logout(request):
	user=request.user
	auth.logout(request)
	return HttpResponse('<h1> %s had logout!</h1>' %user)

