from django.db import models

# Create your models here.
class Login(models.Model):

	mobileno    = models.CharField(max_length=120)
	password = models.CharField(max_length=120)

	def __str__(self):
	    return self.mobileno

	def has_perm(self,perm,obj=None):
		return self.is_superuser
	def has_module_perms(self,app_label):
		return True
