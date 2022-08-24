from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
# Create your models here.

class MyUserManager(BaseUserManager):
	use_in_migrations = True
	def create_user(self,mobileno,password=None,**extra_fields):
		if not mobileno:
			raise ValueError("mobileno required")
		if not password:
			raise ValueError("password required")
		user=self.model(
				mobileno = mobileno,
				**extra_fields
			)
		user.is_superuser=False
		user.is_staff=False
		user.is_admin=True
		user.is_active=True
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,mobileno,password,**extra_fields):
		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_superuser',True)
		extra_fields.setdefault('is_admin',True)
		extra_fields.setdefault('is_active',True)
		if password is None:
			raise TypeError('superuser must have password')

		user=self.create_user( 
			mobileno=mobileno,
			password=password,
			**extra_fields)

		user.is_superuser=True
		user.is_staff=True
		user.is_admin=True
		user.is_active=True
		user.set_password(password)
		user.save(using=self._db)
		return user

class Login(AbstractBaseUser):

    mobileno = models.CharField(verbose_name="Mobile Number",max_length=120,unique=True)
    password = models.CharField(max_length=120)
    is_superuser=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=MyUserManager()
    USERNAME_FIELD="mobileno"
    REQUIRED_FIELDS=[]


    def __str__(self):
        return self.mobileno

    def has_perm(self,perm,obj=None):
        return self.is_superuser
    def has_module_perms(self,app_label):
        return True

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
	if created:
		Token.objects.create(user=instance)