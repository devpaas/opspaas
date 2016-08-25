#coding:utf-8
from django import forms

class ServerForm(forms.Form):
	hostname=forms.CharField(
		max_length=15,
		required=True,
		label=u"主机名",
		error_messages={'required':u'必选项'},
		)
	ip= forms.GenericIPAddressField(
		required=True,
		label=u"IP",
		error_messages={'required':u'必选项'},
		)
	port=forms.IntegerField(
		required=True,
		label='端口',
		error_messages={'required':u'必选项'},
		)
	os=forms.CharField(
		max_length=15,
		label="操作系统",
		required=True,
		error_messages={'required':u'必选项'},
		)
	user=forms.CharField(
		max_length=15,
		label="用户名",
		required=True,
		error_messages={'required':u'必选项'},
		)
	passwd=forms.CharField(
		max_length=15,
		label="密码",
		required=True,
		error_messages={'required':u'必选项'},
		)
	idc=forms.CharField(
		max_length=15,
		required=False,
		label="IDC",
		)
	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError(u"红的标记部分为必选项")
		else:
			cleaned_data=super(ServerForm,self).clean()
		return cleaned_data	


