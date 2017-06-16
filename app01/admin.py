from django.contrib import admin
from models import User,Group,Depart,Work
from django.contrib.auth.hashers import make_password
# Register your models here.

class AppUserAdmin(admin.ModelAdmin):
    fields = ['username','password','usergroup','department','phone','mail_address']
    list_display = ('username', 'usergroup','department','phone','mail_address','c_time')

    def save_model(self, request, obj, form, change):
        obj.password = make_password(form['password'])
        super(AppUserAdmin, self).save_model(request, obj, form, change)

class AppGroupAdmin(admin.ModelAdmin):
    fields = ['groupname']

class AppDepart(admin.ModelAdmin):
    fields = ['departname']

class AppWorkAdmin(admin.ModelAdmin):
    fields = ['workid','title','content','own_user','bind_user']
    list_display = ('workid', 'title', 'own_user', 'bind_user', 'c_time')

admin.site.register(User, AppUserAdmin)
admin.site.register(Group, AppGroupAdmin)
admin.site.register(Depart, AppDepart)
admin.site.register(Work, AppWorkAdmin)