from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse
from rest_framework import status
from .serializers import RegSerializer, LoginSerializer

from .models import Employees
from .forms import EmployeeForm
from hashlib import sha256
from rest_framework.decorators import api_view



@api_view(['GET', 'POST', 'DELETE'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        if len(employees) != 0:
            employee_serializer = RegSerializer(employees, many=True)
            return JsonResponse(employee_serializer.data, safe=False)
        else:
            return JsonResponse({'message': 'There is no employees!'}, status=status.HTTP_204_NO_CONTENT)
        # return render(request, 'reg/employee_list.html', {'Employees' : employees})
    elif request.method =='POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = RegSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED) 
        return JsonResponse({'message': 'User already existed/fields are not valid!'}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Employees.objects.all().delete()
        return JsonResponse({'message' : '{} Users deleted succussfully'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def login(request):
    if request.method == 'POST':
        login_data = JSONParser().parse(request)
        email = login_data['email']
        password = login_data['password']
        login_serializer = Employees.objects.filter(email=email)
        print(login_serializer)
        if login_serializer:
            employee_serializer = RegSerializer(login_serializer, many=True)
            return JsonResponse(employee_serializer.data[0]['description'], safe=False)
        return JsonResponse({'message': 'User is not registered'})
