from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Users  #import the user model from model.py

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields =  ['userId', 'userName', 'email', 'password']
        extra_kwargs = {"password": {"write_only": True}} #extra_kwargs: Makes the password write-only so it is not exposed in API responses.
    def create(self,validated_data): #create: Overridden to hash the password using make_password before saving it to the database. This ensures passwords are securely stored.
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)




