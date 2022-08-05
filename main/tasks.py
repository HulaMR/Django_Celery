from celery import shared_task

from djangoCelery.celery import app
from django.core.mail import send_mail

from .service import send
from .models import Contact

# celery -A djangoCelery flower  --address=127.0.0.6 --port=5566


# my_task.apply_async((2, 3), countdown=60)


@app.task
def send_spam_email(user_email, user):
    send(user_email, user)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            f'Hi {contact.name}. It is Spam!',
            'Spam every 5 minutes!!!',
            'btrealestate12@gmail.com',
            [contact.email],
            fail_silently=False,
        )


@app.task
def my_task(a, b):
    c = a + b
    return c


@app.task(bind=True, default_tetry_delay=5 * 60)
def my_task_retry(self, x, y):
    try:
        return x + y
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@shared_task()
def my_sh_task(msg):
    return msg + '!!!'

