from django.urls import path
from . import views

urlpatterns = [
    # path('', views.users_list, name='post_list'),
    path('api/employees', views.employee_list, name='employee_list'),
    path('api/login', views.login, name='login'),
]