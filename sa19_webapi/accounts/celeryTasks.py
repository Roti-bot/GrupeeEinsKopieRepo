from celery import shared_task

from time import sleep
from django.core.mail import EmailMessage, send_mail


TEMP_EMAIL = "sijare2581@clsn1.com"

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_test():
    sleep(2)
    send_mail('Celery Task Worked!',
    'This is proof the task worked',
    'sa19overwatch@gmail.com',
    [TEMP_EMAIL]  # von tempmail.org
    )
    return None

@shared_task
def send_email_auth(mail_subject, message, to_email):
    sleep(2)  # -> just to see if broker works
    send_mail(mail_subject,
    message,
    'sa19overwatch@gmail.com',
    [to_email]
    )
    return None
