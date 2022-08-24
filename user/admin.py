from django.contrib import admin
from .models import *

# Register your models here.
class LoginAdmin(admin.ModelAdmin):
	list_display =('id','mobileno','password','last_login',"is_staff","is_admin","is_superuser","is_active",)
	fields=('mobileno','password','last_login',"is_staff","is_admin","is_superuser","is_active",)

admin.site.register(Login,LoginAdmin)