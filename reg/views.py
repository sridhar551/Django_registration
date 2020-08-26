from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse
from rest_framework import status, viewsets
from .serializers import UserRegisterSerializer, LoginSerializer
from django.views import View
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

from .models import Employees
from hashlib import sha256

class EmployeeView(View):
    permission_classes = (IsAuthenticated)
    
    def get(self, request):
        employees = Employees.objects.all()
        if len(employees) != 0:
            employee_serializer = UserRegisterSerializer(employees, many=True)
            return JsonResponse(employee_serializer.data, safe=False)
        else:
            return JsonResponse({'message': 'There is no employees!'}, status=status.HTTP_204_NO_CONTENT)
        # return render(request, 'reg/employee_list.html', {'Employees' : employees})

    def post(self, request):
        employee_data = JSONParser().parse(request)
        employee_serializer = UserRegisterSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse({'message': employee_serializer.data}, status=status.HTTP_201_CREATED) 
        return JsonResponse({'message': 'User already existed/fields are not valid!'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        count = Employees.objects.all().delete()
        return JsonResponse({'message' : '{} Users deleted succussfully'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

class LoginView(View):
    # permission_classes = (IsAuthenticated)

    def post(self, request):
        login_data = JSONParser().parse(request)
        email = login_data['email']
        password = login_data['password']
        user = authenticate(email=email, password=password)
        login_serializer = Employees.objects.filter(email=email, password=password)
        if login_serializer:
            employee_serializer = UserRegisterSerializer(login_serializer, many=True)
            description = employee_serializer.data[0]['description']
            return JsonResponse({'description' : description}, status=status.HTTP_201_CREATED)
        return JsonResponse({'message': 'User is not registered'})


"""from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import serializers
from .utils import get_and_authenticate_user, create_user_account



class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login': serializers.LoginSerializer,
        'register': serializers.UserRegisterSerializer
    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()"""