from django.utils import timezone
from django.contrib.auth import authenticate
from rest_framework import mixins, viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.schemas import ManualSchema

from .serializers import AuthTokenSerializer, UserRegistrationSerializer, UserSerializer
from users.models import User


class UserTokenViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            data=UserSerializer(data=user)
        )

    @action(
        methods=['post'],
        detail=False,
        permission_classes=(~IsAuthenticated,),
    )
    def login(self, request, *args, **kwargs):
        """
        Create user authorization token.
        """
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['obj']
        if code.used:
            # Проверка: Не был ли код активирован
            # ранее (поле used = False).
            return Response(
                data='The code has used.',
                status=status.HTTP_400_BAD_REQUEST
            )
        if code.datetime_end < timezone.now():
            # Проверка: Код действует (текущая дата
            # меньше чем дата в поле datetime_end).
            return Response(
                data='The code has expired.',
                status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.get(email=request.data['email'])
        token, created = Token.objects.get_or_create(user=user)
        # После создания токена меняем статус used на True.
        code.used = True
        code.save()
        return Response({'token': token.key})

    @action(
        methods=['delete'],
        detail=False,
        permission_classes=(IsAuthenticated,),
    )
    def logout(self, request, *args, **kwargs):
        """
        Delete user authorization token.
        """
        # Удалить токен.
        user_token = request.user.auth_token
        user_token.delete()
        return Response(
            data='The authorization token has been removed.',
            status=status.HTTP_204_NO_CONTENT

        )
