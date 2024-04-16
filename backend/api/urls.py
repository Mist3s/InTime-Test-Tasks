from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

from .views import UserViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/docs/', TemplateView.as_view(
        template_name='docs/redoc.html',
        content_type='text/html'
    )),
    path('v1/docs/openapi-schema.yml', TemplateView.as_view(
        template_name='docs/openapi-schema.yml',
        content_type='text/yaml'
    )),

]
