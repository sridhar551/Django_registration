from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import Http404
# from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Employees
from .serializers import UserRegisterSerializer, LoginSerializer


class EmployeeView(APIView):
    
    def get(self, request):
        try:
            employees = Employees.objects.all()
            serializer = UserRegisterSerializer(employees, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            employee_data = request.data
            print (employee_data)
            serializer = UserRegisterSerializer(data=employee_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': serializer.data}, status=status.HTTP_201_CREATED) 
            return Response({'message': 'User already existed/fields are not valid!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            count = Employees.objects.all().delete()
            return JsonResponse({'message' : '{} Users deleted succussfully'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'result': 'False'}), 500
        

class EmployeeDetail(APIView):

    def get_object(self, pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            return Response({'message': 'User Does not existed'})

    def get(self, request, pk):
        try:
            employee = self.get_object(pk)
            serializer = UserRegisterSerializer(employee)
            return Response(serializer.data)
        except:
            return Response({'message': 'User Does not existed'})

    def put(self, request, pk):
        try:
            employee = self.get_object(pk)
            serializer = UserRegisterSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            employee = self.get_object(pk)
            employee.delete()
            return Response({'message': 'User Deleted successfully'})
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    def post(self, request):
        try:
            login_data = request.data            
            email = login_data['email']            
            password = login_data['password']
            serializer = Employees.objects.get(email=email)            
            if serializer:
                employee_serializer = UserRegisterSerializer(serializer)
                description = employee_serializer.data['description']
                return Response({'description' : description}, status=status.HTTP_201_CREATED)            
        except:
            return Response({'message': 'User not existed'})


