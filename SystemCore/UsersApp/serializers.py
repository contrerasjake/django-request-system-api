from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers
from .models import UserInformation
from django.contrib.auth.models import User

class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'FirstName',
            'LastName',
            'MiddleName',
            'Address',
            'Email',
            'MobileNumber',
            'date_created',
        )
        model = UserInformation
        
class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=65, min_length=8, write_only=True)
    email=models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    first_name=models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)
    last_name=models.ForeignKey(to=UserInformation, on_delete=models.CASCADE)

    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email=attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']