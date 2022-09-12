from django.urls import path
from rest_framework import routers
from .views import UserRegister, UserLogin, RecoveryPassword
#
router = routers.SimpleRouter()
router.register(r'register', UserRegister, basename='register')
router.register(r'login', UserLogin, basename='login')
router.register(r'recovery', RecoveryPassword, basename='recovery')
#
urlpatterns = []

urlpatterns += router.urls
