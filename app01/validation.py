#coding:utf8
from django import forms
from models import User
from django.core.validators import ValidationError

def phone_exist_validator(value):
    try:
        user = User.objects.get(phone=value)
        raise ValidationError(u'电话号码已存在')
    except:
        pass

def mail_exist_validator(value):
    try:
        user = User.objects.get(mail_address=value)
        raise ValidationError(u'邮箱地址已存在')
    except:
        pass

def username_exist_validator(value):
    try:
        user = User.objects.get(username=value)
        raise ValidationError(u'用户名已存在')
    except:
        pass



