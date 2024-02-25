import random

from celery import shared_task
from django.core.mail import send_mail

from engineer.models import Term


@shared_task
def send_email_task(subject: str, message: str):
    send_mail(
        subject=subject,
        message=message,
        from_email='admin@moeinarabi.ir',
        recipient_list=['moein.mo81@gmail.com'],
        fail_silently=False,
    )


@shared_task
def send_random_terms_periodic_task():
    terms = get_random_terms()
    send_email_task('Review your random terms', ', '.join(terms))


def get_random_terms() -> list:
    terms = list(Term.objects.values_list('name', flat=True))
    random.shuffle(terms)
    return terms[:5]
