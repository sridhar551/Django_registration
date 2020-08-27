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
        fields = ('id', 'name', 'email', 'password', 'description')

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = ('email', 'password')

class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
         model = Employees
         fields = all
    
    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key

class EmptySerializer(serializers.Serializer):
    pass