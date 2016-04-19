#coding:utf-8
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from models import *
from forms import AddForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
def login(request):
	return render_to_response('login.html')
def index(request):
        return render_to_response('index.html')

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


def logout(request):
	user=request.user
	auth.logout(request)
	return HttpResponse('<h1> %s had logout!</h1>' %user)

def server_manager(request):
	servers_list=Servers.objects.order_by("-id").all()
        return render_to_response('server_manager.html',{'servers_list':servers_list})

def ssh2(ip,port,username,password,cmd):
	try:
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko,AutoAddPolicy())      #允许不连接know_hosts文件中的主机
		ssh.connect("ip","port","username","password",timeout=5)
		stdin,stdout,stderr=ssh.exec_command(cmd)
		print stdout.read()
		print 'stOKn' % (ip)
	except:
		print '%stErrorn' % (ip)

def addserver(request):
	if request.method=='POST':
		form=AddForm(request.POST)      #绑定表单
		if form.is_valid():
			s=Servers.objects.create(		#生成数据对象,自动保存到数据库中	
			hostname=form.cleaned_data['hostname'],
			ip=form.cleaned_data['ip'],				
			port=form.cleaned_data['port'],
			os=form.cleaned_data['os'],
			idc=form.cleaned_data['idc'],
			)
			data=form.cleaned_data
			return HttpResponseRedirect('/server_manager/')
	else: 
		form=AddForm()
	return render_to_response('addserver.html',{'form':form})

def delete_server(request):
	ip=request.GET['ip'];
	q_ip=Servers.objects.get(ip=ip)
	q_ip.delete()
	return HttpResponseRedirect('/server_manager/')

#删除所选：
def delselect(request):
	arr=request.GET['arr']
	blist="("+arr+")"          #根据列表构建元组
	Servers.objects.extra(where=['ip IN' +str(blist)+'']).delete()
	return HttpResponse("删除成功")
def queryByIP(request):
	ip=request.GET['ip']
	print ip
	if ip=="":
		return HttpResponseRedirect('/server_manager/')
	bb=Servers.objects.filter(ip=ip)
	return render_to_response('server_manager.html',{'servers_list':servers_list})

#查询所有，并分页显示
def query(request):
	limit = 5
	servers_list=Servers.objects.all()
	paginator=Paginator(servers_list,limit) 
	page=request.GET.get('page')
	try:
		servers_list=paginator.page(page) #获取某页对应的记录数
	except PageNotAnInteger: #如果页码不是整数
		servers_list=paginator.page(1)
	except EmptyPage:  #如果页码太大，没有相应的记录
		servers_list=paginator.page(paginator.num_pages) #取最后一页的记录
	return render_to_response('server_manager.html',{'servers_list':servers_list})
