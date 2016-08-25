#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Servers(models.Model):
	hostname=models.CharField(max_length=50,unique=True)
	ip=models.GenericIPAddressField(unique=True)
	idc=models.CharField(max_length=20,null=True,blank=True)     #blank=True表示表单可以为空
	port=models.IntegerField(default='22')
	os=models.CharField(max_length=20,default='linux',verbose_name='Operating System')  #verbose_name自述名
	user=models.CharField(max_length=20,default='root',verbose_name='manage user')
	passwd=models.CharField(max_length=20,verbose_name='manage passwd')
	is_checked=models.BooleanField(default=False)
	def __unicode__(self):
		return self.hostname
		return self.ip
		return self.idc
		return self.port
		return self.os
		return self.user
		return self.passwd
	
class UserInfo(models.Model):
	username=models.CharField(max_length=10)
