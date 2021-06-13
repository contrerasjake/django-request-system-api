from rest_framework import serializers
from .models import UserInformation, User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class UserInformationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserInformation
        fields = ('MiddleName', 'Address', 'MobileNumber', 'resident_number', 'date_of_birth', 'age', 'gender', 'province', 'civil_status')
class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserInformationSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserInformation.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.MiddleName = profile_data.get('MiddleName', profile.MiddleName)
        profile.Address = profile_data.get('Address', profile.Address)
        profile.MobileNumber = profile_data.get('MobileNumber', profile.MobileNumber)
        profile.resident_number = profile_data.get('resident_number', profile.resident_number)
        profile.date_of_birth = profile_data.get('date_of_birth', profile.date_of_birth)
        profile.age = profile_data.get('age', profile.age)
        profile.gender = profile_data.get('gender', profile.gender)
        profile.province = profile_data.get('province', profile.province)
        profile.civil_status = profile_data.get('civil_status', profile.civil_status)
        profile.save()

        return instance

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')