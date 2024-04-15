import random
import string

from django.core.mail import send_mail


def generate_authorization_code(length=6):
    """Authorization code generator."""
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))


def send_mail_confirmation_code(user, authorization_code):
    """Sending authorization code to the user by email."""
    send_mail(
        subject='Authorization code.',
        message=(
            f'Your authorization code: {authorization_code}'
        ),
        recipient_list=[user.email],
        from_email='test@mail.ru',
        fail_silently=True,
    )
