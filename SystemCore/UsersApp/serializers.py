from django.db import models
from rest_framework import serializers
from .models import UserInformation

class UserSerializer(serializers.ModelSerializer):
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