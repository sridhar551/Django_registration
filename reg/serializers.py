from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from reg.models import Employees

# User = Employees
# print(User)
class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employees
        fields = ('name', 'email', 'password', 'description')

    def validate_email(self, value):
        user = Employees.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already registered")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = ('email', 'password')

class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
         model = Employees
         fields = ('id', 'email', 'name', 'description', 'is_active', 'is_staff')
         read_only_fields = ('id', 'is_active', 'is_staff')
    
    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key

class EmptySerializer(serializers.Serializer):
    pass