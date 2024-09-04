import random

import telebot
from digikala_api import product_detail
from celery import shared_task
from django.core.mail import send_mail

from toolbox.settings.base import TELEGRAM_BOT_TOKEN, TELEGRAM_OWNER_CHATID
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
def send_digikala_product_task(product_id: str):
    product = product_detail(product_id)
    message = f'{product.persian_name}\n{product.price}\n\n{product.url}'
    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode=None)
    bot.send_message(TELEGRAM_OWNER_CHATID, message)


@shared_task
def send_random_terms_periodic_task():
    terms = get_random_terms()
    send_email_task('Review your random terms', ', '.join(terms))


def get_random_terms() -> list:
    terms = list(Term.objects.values_list('name', flat=True))
    random.shuffle(terms)
    return terms[:5]
