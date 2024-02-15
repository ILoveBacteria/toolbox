from django.core.mail import send_mail

from django_cron import CronJobBase, Schedule


class SendMailCron(CronJobBase):
    RUN_EVERY_MINS = 2  # every week
    RETRY_AFTER_FAILURE_MINS = 30

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'engineer.SendMailCron'

    def do(self):
        send_mail(
            'Review your terms',
            'Sample text',
            'admin@moeinarabi.ir',
            ['moein.mo81@gmail.com'],
            fail_silently=False,
        )
