from .serializers import *
from user.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets , status
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly , AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.views import obtain_auth_token



class Newuser(viewsets.ModelViewSet):
	permission_classes=[AllowAny,]
	serializer_class= LoginSerializer
	def create(self,request):
		mobileno=request.data['mobileno']
		if Login.objects.filter(mobileno=mobileno).first():
			return Response("User Already Exist")
		serializer = LoginSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response("created Successfully",status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Userlist(viewsets.ViewSet):
	permission_classes=( IsAuthenticated,)
	def list(self , request):
		user = request.user
		if user.is_superuser:
			queryset = Login.objects.all()
			serializer = LoginSerializer(queryset,many=True)
			return Response(serializer.data)
		return Response("No Permissions for Normal User")

class Loginview(viewsets.ViewSet):
	permission_classes=(IsAuthenticated,)
	def retrieve(self,request):
		try:
			mobileno= request.user
			users = Login.objects.filter(mobileno=mobileno).first()
			pk=users.id
			queryset= Login.objects.get(id=pk)
			user = request.user
			if user != queryset:
				return Response({'response':"You Dont Have permissions to See user data"})
			serializer = LoginSerializer(queryset,many=False)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		except Login.DoesNotExist:
			return Response("Not Found")
	def update(self,request,pk):
		try:
			queryset= Login.objects.get(id=pk)
			user = request.user
			if queryset != user:
				return Response({'response':"You Dont Have permissions to update"})
			serializer = LoginSerializer(instance=queryset,data=request.data)
			if serializer.is_valid():
				serializer.save()
			return Response(serializer.data)
		except Login.DoesNotExist:
			return Response("Not Found")


	def partialupdate(self,request,pk):
		try:
			queryset= Login.objects.get(id=pk)
			user = request.user
			if (queryset != user) ^ (queryset.is_superuser != user.is_superuser):
				return Response({'response':"You Dont Have permissions to update"})
			serializer = LoginSerializer(instance=queryset,data=request.data,partial=True)
			if serializer.is_valid(raise_exception=True):
				serializer.save()
			return Response(serializer.data)
		except Login.DoesNotExist:
			return Response("Not Found")


	def delete(self,request,pk):
		try:
			queryset= Login.objects.get(id=pk)
			user = request.user
			if (queryset != user) ^ (queryset.is_superuser != user.is_superuser):
				return Response({'response':"You Dont Have permissions to delete"})
			queryset.delete()
			return Response("Deleted Successfully")
		except Login.DoesNotExist:
			return Response("Not Found")
    
	def passwordupdate(self,request,pk):
		try:
			queryset= Login.objects.get(id=pk)
			user = request.user
			old_pwd=request.data['old_pwd']
			if user.check_password(old_pwd):
				if queryset != user:
					return Response({'response':"You Dont Have permissions to update"})
				serializer = PasswordSerializer(instance=queryset,data=request.data,partial=True)
				if serializer.is_valid(raise_exception=True):
					serializer.save()
					return Response("Password Changed Successfully")
			else:
				return Response("Check Old Password")
		except Login.DoesNotExist:
			return Response("Not Found")	

    