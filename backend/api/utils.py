import random
import string

from django.core.mail import send_mail


def generate_authorization_code(length=6):
    """Authorization code generator."""
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))
