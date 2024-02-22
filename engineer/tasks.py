from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_feedback_email_task(message):
    send_mail(
        'Review your terms',
        message,
        'admin@moeinarabi.ir',
        ['moein.mo81@gmail.com'],
        fail_silently=False,
    )
