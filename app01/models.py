#coding:utf8
from __future__ import unicode_literals
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.


class Group(models.Model):
    groupname = models.CharField(max_length=50,unique=True)

    def __unicode__(self):
        return self.groupname


class Depart(models.Model):
    departname = models.CharField(max_length=50,unique=True)


    def __unicode__(self):
        return self.departname

class User(AbstractBaseUser):
    username = models.CharField(max_length=20,null=False,unique=True)
    password = models.CharField(max_length=128,null=True)
    usergroup = models.ForeignKey(Group)
    department = models.ForeignKey(Depart)
    c_time = models.DateTimeField(auto_now_add=True)
    m_time = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20,null=True,unique=True)
    mail_address = models.CharField(max_length=50,null=True,unique=True)

    is_staff = False
    has_module_perms = False

    def __unicode__(self):
        return self.username



    # def check_password(self,this_password):
    #     if self.password == make_password(this_password):
    #         return True
    #     else:
    #         return False



class Work(models.Model):
    workid = models.IntegerField()
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=255)
    own_user = models.ForeignKey(User,related_name='own_user',verbose_name='绑定用户')
    bind_user = models.ForeignKey(User,related_name='bind_user')
    c_time = models.DateTimeField(auto_now_add=True)
    m_time = models.DateTimeField(auto_now=True)
    f_time = models.DateTimeField()

    def __unicode__(self):
        return self.title