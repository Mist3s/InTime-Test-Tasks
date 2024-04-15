from django.utils import timezone
from rest_framework import mixins, viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.hashers import make_password

from .serializers import (
    AuthTokenSerializer,
    UserRegistrationSerializer,
    UserSerializer
)
from users.models import User


class UserTokenViewSet(mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    @action(
        methods=['GET'],
        detail=False,
        permission_classes=(IsAuthenticated,),
        url_path='me'
    )
    def get_current_user_info(self, request):
        serializer = UserSerializer(request.user)
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

    @get_current_user_info.mapping.patch
    def update_user_info(self, request):
        serializer = UserSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    @get_current_user_info.mapping.delete
    def delete_user(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        hasher_password = make_password(
            password,
            salt=None,
            hasher='default'
        )
        serializer.save(
            password=hasher_password
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
