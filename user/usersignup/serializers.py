
from rest_framework import serializers
from user.models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class LoginSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    mobileno=serializers.CharField(max_length=120, required=True)
    password=serializers.CharField(write_only=True)
    is_active=serializers.BooleanField(default=True)
    is_admin=serializers.BooleanField(default=True)
    is_staff=serializers.BooleanField(default=True)


    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance

    def partialupdate(self,instance,validated_data):
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance

    class Meta:
         model = Login
         fields = ["id","mobileno","password","is_staff","is_admin","is_superuser","is_active",]
        
