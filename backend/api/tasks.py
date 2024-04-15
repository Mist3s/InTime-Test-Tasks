from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_confirmation_code(email, authorization_code):
    """Sending authorization code to the user by email."""
    mail = send_mail(
        subject='Authorization code.',
        message=(
            f'Your authorization code: {authorization_code}'
        ),
        recipient_list=[email],
        from_email='test@mail.ru',
        fail_silently=True,
    )
    return mail
