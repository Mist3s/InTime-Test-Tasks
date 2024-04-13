from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

REGEX_SIGNS = RegexValidator(
    regex=r'^[\w.@+-]+\Z',
    message='Поддерживаемые символы.'
)
REGEX_ME = RegexValidator(
    regex=r'[^m][^e]',
    message='Имя пользователя не может быть "me".'
)


class User(AbstractUser):
    """
    Модель пользователей.
    """
    username = models.CharField(
        unique=True,
        max_length=150,
        validators=(REGEX_SIGNS, REGEX_ME),
        verbose_name='Никнейм пользователя',
        help_text='Укажите никнейм пользователя.'
    )
    email = models.EmailField(
        unique=True,
        max_length=254,
        verbose_name='E-mail пользователя',
        help_text='Укажите e-mail пользователя.'
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        help_text='Укажите имя пользователя.'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия пользователя',
        help_text='Укажите фамилию пользователя.'
    )
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class AuthCode(models.Model):
    """
    Модель кода авторизации.
    """
    code = models.CharField(
        max_length=6,
        verbose_name='Код авторизации'
    )
    user = models.ForeignKey(
        User,
        related_name='auth_codes',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    datetime_end = models.DateTimeField(
        verbose_name='Время действия'
    )
    used = models.BooleanField(
        default=False,
        verbose_name='Использован'
    )

    class Meta:
        ordering = ('-datetime_end',)
        verbose_name = 'Код активации'
        verbose_name_plural = 'Коды активации'

    def __str__(self):
        return f'{self.code}/{self.used}'
