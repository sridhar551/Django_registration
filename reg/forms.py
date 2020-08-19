from django import forms
from reg.models import Employees
# from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta():
#         model = User
#         fields = ('username', 'password', 'email')

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = ('email', 'password',)