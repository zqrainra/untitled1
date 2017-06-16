from django.shortcuts import render,redirect
from django.http import HttpResponse
from form import WorkForm,UserForm,GroupForm,DepartForm
from models import Work,User,Group,Depart
from django.forms import modelformset_factory,modelform_factory
# Create your views here.

def index(request):
    if request.method == 'GET':
        works = Work.objects.all()
        context = {'works':works}
        return render(request,'app01/index.html',context=context)

def list_users(request):
    if request.method == 'GET':
        users = User.objects.filter(usergroup='2')
        context = {"users":users}
        return render(request,'app01/list_user.html',context=context)


def add_users(request):

    if request.method == 'GET':
        groups = Group.objects.all()
        departments = Depart.objects.all()
        form = UserForm()
        context = {
            'groups':groups,
            'departments':departments,
            'form':form
        }
        return render(request,'app01/add_user.html',context=context)
    elif request.method == 'POST':

        form = UserForm(
            request.POST
        )
        print(request.POST)
        if form.is_valid():
            form.save()

        return redirect( 'add_users')