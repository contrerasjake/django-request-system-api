from rest_framework import serializers, status
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password

class UserInformationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email',
                  'first_name', 
                  'middle_name', 
                  'last_name', 
                  'address', 
                  'mobile_number', 
                  'resident_number',
                  'date_of_birth',
                  'age',
                  'gender',
                  'province',
                  'civil_status',
                  'profile_pic',
                  'id_pic',
                 ]

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:

        model = User
        fields = ['email', 
                  'first_name', 
                  'middle_name', 
                  'last_name', 
                  'password', 
                  'address', 
                  'mobile_number', 
                  'resident_number',
                  'date_of_birth',
                  'age',
                  'gender',
                  'province',
                  'civil_status',
                  'profile_pic',
                  'id_pic',
                  ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class AccountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'is_admin', 'is_email_verified']

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(LoginSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': self.user.email})
        data.update({'status': self.user.is_email_verified})
        return data

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {
        'bad_token': ('Token is expired or invalid')
    }
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            raise serializers.ValidationError({'details': ('Token is expired or invalid')})

class ChangePasswordSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password = serializers.CharField(write_only=True, min_length=8, required=True)
    password2 = serializers.CharField(write_only=True, min_length=8, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance