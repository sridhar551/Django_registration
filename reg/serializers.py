from rest_framework import serializers
from reg.models import Employees

class RegSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employees
        fields = ('name', 'email', 'password', 'description')

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = ('email', 'password')