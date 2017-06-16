#coding:utf8
from django.forms import ModelForm
from models import User,Group,Work,Depart
from django import forms
from django.core.exceptions import ValidationError
from .validation import username_exist_validator,mail_exist_validator,phone_exist_validator

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','usergroup','department','phone','mail_address']

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['groupname']

class DepartForm(ModelForm):
    class Meta:
        model = Depart
        fields = ['departname']

class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ['workid','title','content','bind_user','own_user']

class CreateUserForm(forms.Form):
    username = forms.CharField(required=True,error_messages={'required':u'用户名不能为空'},
                               validators=[username_exist_validator,])
    password = forms.CharField(required=True,error_messages={'required':u'密码不能为空'})
    usergroup = forms.CharField(required=True,error_messages={'required':u'用户组不能为空'})
    department = forms.CharField(required=True,error_messages={'required':u'部门不能为空'})
    phone = forms.CharField(validators=[])

