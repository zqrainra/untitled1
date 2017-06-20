from django.shortcuts import render,redirect
from django.http import HttpResponse
from form import WorkForm,UserForm,GroupForm,DepartForm
from models import Work,User,Group,Depart
from django.forms import modelformset_factory,modelform_factory
from .form import CreateUserForm,GroupForm
import json
# Create your views here.

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

def add_group(request):
    if request.method == 'POST':
        context = {}
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            print(group)
            context = {'group':group.id}
            return HttpResponse(json.dumps(context))
    else:
        form = GroupForm()
    return render(request,'app01/add_group.html',{'form':form})

def add_department(request):
    pass


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