#coding:utf8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from form import WorkForm,UserForm,GroupForm,DepartForm,LoginForm
from models import Work,User,Group,Depart
from django.forms import modelformset_factory,modelform_factory
from .form import CreateUserForm,GroupForm
import json
from backends import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/user_login/')
def index(request):
    if request.method == 'GET':
        works = Work.objects.all()
        context = {'works':works}
        return render(request,'app01/index.html',context=context)

def list_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        context = {"users":users}
        return render(request,'app01/list_user.html',context=context)

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=request.POST['username'],password=request.POST['password'])
            if user:
                login(request,user)
                return redirect(index)
            else:
                login_form.errors['password'] = u'用户名或密码错误'
    else:
        if request.user.is_authenticated:
            print(request.user)
            return redirect(index)
        login_form = LoginForm()
    context = {'form':login_form}
    return render(request,'app01/login.html',context=context)

def user_logout(request):
    logout(request)
    return redirect('user_login')



def add_group(request):
    if request.method == 'POST':
        print(request.POST)
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            print(group)
            context = {'context':[group.id,group.groupname]}
        else:
            context = {'errors':form.errors}
        return HttpResponse(json.dumps(context))
    else:
        form = GroupForm()
    return render(request,'app01/add_group.html',{'form':form})

def add_department(request):
    if request.method == 'POST':
        print(request.POST)
        form = DepartForm(request.POST)
        if form.is_valid():
            depart = form.save()
            print(depart)
            context = {'context':[depart.id,depart.departname]}
        else:
            context = {'errors':form.errors}
        return HttpResponse(json.dumps(context))
    else:
        form = DepartForm()
    return render(request,'app01/add_depart.html',{'form':form})


def add_users(request):
    groups = Group.objects.all()
    departments = Depart.objects.all()
    sucess = False
    if request.method == 'GET':
        form = UserForm()

    elif request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = UserForm()
                sucess = True
            except Exception as e:
                print(e)
        else:
            print(form.errors)
    context = {
        'groups': groups,
        'departments': departments,
        'form': form,
        'sucess':sucess,
    }

    return render(request, 'app01/add_user.html', context=context)

        # return redirect( 'add_users')