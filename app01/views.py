from django.shortcuts import render,redirect
from django.http import HttpResponse
from form import WorkForm,UserForm,GroupForm,DepartForm
from models import Work,User,Group,Depart
from django.forms import modelformset_factory,modelform_factory
from .form import CreateUserForm
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
    groups = Group.objects.all()
    departments = Depart.objects.all()
    if request.method == 'GET':
        form = UserForm()

    elif request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            print(form.clean())
        else:
            print(form.errors)
    context = {
        'groups': groups,
        'departments': departments,
        'form': form
    }
    print(int(form['usergroup'].value()) == groups[0].id)
    return render(request, 'app01/add_user.html', context=context)

        # return redirect( 'add_users')