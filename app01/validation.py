#coding:utf8
from django import forms
from models import User
from django.core.validators import ValidationError

def phone_exist_validator(value):
    user = User.objects.get(phone=value)
    if user :
        raise ValidationError(u'电话号码已存在')

def mail_exist_validator(value):
    user = User.objects.get(mail_address=value)
    if user :
        raise ValidationError(u'邮箱地址已存在')

def username_exist_validator(value):
    user = User.objects.get(username=value)
    if user :
        raise ValidationError(u'用户名已存在')
