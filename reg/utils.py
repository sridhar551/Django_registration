from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
# from django.contrib.auth import get_user_model
from .models import Employees

# User = Employees

def get_and_authenticate_user(email, password):
    user = authenticate(email=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user

def create_user_account(name, email, password, description, **extra_fields):
    user = Employees.objects.create_user(username=name, email=email,
        password=password, description=description, **extra_fields)
    return user
    