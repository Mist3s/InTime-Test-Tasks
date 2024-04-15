from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from users.models import User, AuthCode


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    code = serializers.CharField(
        label=_("Code"),
        # style={'input_type': 'password'},
        # trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')

        if email and code:
            obj = AuthCode.objects.filter(
                user__email=email,
                code=code
            ).first()
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # user_api.)
            if not obj:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "code".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['obj'] = obj
        return attrs


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )

    def to_representation(self, instance):
        """Переопределение сериализатора для выходных данных."""
        return UserShortSerializer(
            instance, context=self.context
        ).data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )


class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
        )
