from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import UserTokenViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', UserTokenViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),

]