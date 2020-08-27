from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    # path('', views.users_list, name='post_list'),
    path('api/employees', views.EmployeeView.as_view()),
    path('api/login', views.LoginView.as_view()),
    path('api/employees/<int:pk>', views.EmployeeDetail.as_view()),
]
