from django.contrib import admin
from .models import *

# Register your models here.
class LoginAdmin(admin.ModelAdmin):
	list_display =('id','mobileno','password','last_login',)
	fields=('mobileno','password','last_login',)

admin.site.register(Login,LoginAdmin)