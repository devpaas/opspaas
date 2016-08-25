#encoding:utf-8
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from models import *
from forms import ServerForm
#添加django自带的分页插件paginator
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def server_manage(request):
    limit=5 # 每页显示的记录数
    servers_list=Servers.objects.order_by("-id").all()
    paginator=Paginator(servers_list,limit)    #创建一个分页器对象
    page=request.GET.get('page') #获取页码
    try:
        servers_list=paginator.page(page)  #获取某页的记录
    except PageNotAnInteger:
        servers_list=paginator.page(1)  #如果页码不是整数，取第一页的记录
    except EmptyPage:
        servers_list=paginator.page(paginator.num_pages)     #如果页码太大，取最后一页数据
    return render_to_response('sm/server_manage.html',{'servers_list':servers_list})

def addserver(request):
	if request.method=='POST':
		form=ServerForm(request.POST)      #将提交的请求数据，绑定为表单
		print form
		if form.is_valid():             #用表单的方法校验数据是否合法
			Servers.objects.create(		#生成数据对象,自动保存到数据库中
			hostname=form.cleaned_data['hostname'],
			ip=form.cleaned_data['ip'],
			port=form.cleaned_data['port'],
			os=form.cleaned_data['os'],
			user=form.cleaned_data['user'],
			passwd=form.cleaned_data['passwd'],
			idc=form.cleaned_data['idc'],
			)
			return HttpResponseRedirect('/sm/server_manage')
	else:
		form=ServerForm()
	return render_to_response('sm/addserver.html',{'form':form})   #模板目录

#删除单台主机
def del_server(request):
	ip=request.GET['ip']
	q_ip=Servers.objects.get(ip=ip)
	q_ip.delete()
	return HttpResponseRedirect('/sm/server_manage')

#批量删除主机
def batch_del(request):
	if request.method=='POST':
		ids=request.POST.get('ids')          #接受request的数据，从post中取得数据
		Servers.objects.extra(where=['id IN ('+ids+')']).delete()   #extra传递多个where的参数
	return HttpResponseRedirect('/sm/server_manage')

#根据IP查询主机信息
def queryIP(request):
	ip=request.GET.get('ip')
	if ip=="":
		return HttpResponseRedirect('/sm/server_manage')
	else:
		q=Servers.objects.filter(ip=ip)  #filte返回的是一个列表对象，object.get返回的是一个字典
		return render_to_response('sm/server_manage.html',{'servers_list':q})

def edit_server(request):
	id=request.GET.get('id')
	host_form=Servers.objects.filter(id=id)       #查询出id对应的主机
	if	request.method=='POST':
		form=ServerForm(request.POST)      #绑定表单
		if form.is_valid():             #如果提交的数据合法
			Servers.objects.filter(id=id).update(		#filter返回一个对象列表,用update更新数据库中的条目
			hostname=form.cleaned_data['hostname'],
			ip=form.cleaned_data['ip'],
			port=form.cleaned_data['port'],
			os=form.cleaned_data['os'],
			user=form.cleaned_data['user'],
			passwd=form.cleaned_data['passwd'],
			idc=form.cleaned_data['idc'],
			)
			return HttpResponseRedirect('/sm/server_manage')
	else:
		form=ServerForm()
	return render_to_response('sm/edit_server.html',{'form':host_form})



