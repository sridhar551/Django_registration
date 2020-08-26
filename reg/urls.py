from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    # path('', views.users_list, name='post_list'),
    path('api/employees', csrf_exempt(views.EmployeeView.as_view())),
    path('api/login', csrf_exempt(views.LoginView.as_view())),
]

"""from rest_framework import routers

from .views import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')

urlpatterns = router.urls"""