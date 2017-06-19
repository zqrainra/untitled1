#coding:utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Group(models.Model):
    groupname = models.CharField(max_length=50)

    def __unicode__(self):
        return self.groupname


class Depart(models.Model):
    departname = models.CharField(max_length=50)


    def __unicode__(self):
        return self.departname

class User(models.Model):
    username = models.CharField(max_length=20,null=False,unique=True)
    password = models.CharField(max_length=128,null=True)
    usergroup = models.ForeignKey(Group)
    department = models.ForeignKey(Depart)
    c_time = models.DateTimeField(auto_now_add=True)
    m_time = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20,null=True,unique=True)
    mail_address = models.CharField(max_length=50,null=True,unique=True)

    def __unicode__(self):
        return self.username


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