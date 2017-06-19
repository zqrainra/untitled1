#coding:utf8
from django.forms import ModelForm
from models import User,Group,Work,Depart
from django import forms
from django.core.exceptions import ValidationError
from .validation import username_exist_validator,mail_exist_validator,phone_exist_validator
from django.contrib.auth.hashers import make_password

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','usergroup','department','phone','mail_address']

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['groupname']
    def clean(self):
        if self.validate_unique():
            raise ValidationError('用户组已存在')



class DepartForm(ModelForm):
    class Meta:
        model = Depart
        fields = ['departname']


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ['workid','title','content','bind_user','own_user']

class CreateUserForm(forms.Form):
    username = forms.CharField(required=True,error_messages={'required':u'用户名不能为空'},)
    password = forms.CharField(required=True,error_messages={'required':u'密码不能为空'})
    usergroup = forms.CharField(required=True,error_messages={'required':u'用户组不能为空'})
    department = forms.CharField(required=True,error_messages={'required':u'部门不能为空'})
    phone = forms.CharField(required=True,error_messages={'required':u'电话号码不能为空'},)
    mail_address = forms.CharField(required=True,error_messages={'required':u'邮箱地址不能为空'},)

    def clean_password(self):
        password = make_password(self.cleaned_data['password'])
        return password

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if user:
            raise ValidationError(u'用户名已存在')
        return username

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = User.objects.filter(phone=phone)
        if user:
            raise forms.ValidationError(u'电话已存在')
        return phone

    def clean_mail_address(self):
        mail_address = self.cleaned_data['mail_address']
        user = User.objects.filter(mail_address=mail_address)
        if user:
            raise forms.ValidationError(u'邮箱已存在')
        return mail_address

    def save(self):
        try:
            usergroup = Group.objects.get(id=self.cleaned_data['usergroup'])
            department = Depart.objects.get(id=self.cleaned_data['department'])
            self.cleaned_data.pop('usergroup')
            self.cleaned_data.pop('department')
            user = User(usergroup=usergroup,department=department,**self.cleaned_data)
            user.save()
            return user
        except Exception as e:
            raise e
