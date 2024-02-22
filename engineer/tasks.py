from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_term_email_task(message: str):
    send_mail(
        subject='Review your terms',
        message=message,
        from_email='admin@moeinarabi.ir',
        recipient_list=['moein.mo81@gmail.com'],
        fail_silently=False,
    )
