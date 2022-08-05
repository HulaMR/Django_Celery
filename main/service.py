from django.core.mail import send_mail
from django.template.loader import render_to_string


def send(user_email, user):
    email = render_to_string('main/email.html', {'user': user})
    send_mail(
        f'Hi {user}. You follow for resend',
        'Test!!!',
        'btrealestate12@gmail.com',
        [user_email],
        fail_silently=False,
        html_message=email

    )
