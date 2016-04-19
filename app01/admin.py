#coding:utf-8
from django.contrib import admin
from django.contrib.auth.models import User as djangouser,Group as djangogroup
from app01.models import *



# Register your models here.
admin.site.register(Servers)                  #注册数据库到后台管理中

