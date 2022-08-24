from django.contrib import admin
from .models import *

# Register your models here.
class LoginAdmin(admin.ModelAdmin):
	list_display =('id','mobileno','password',)

admin.site.register(Login,LoginAdmin)