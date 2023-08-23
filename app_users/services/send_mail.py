from django.conf import settings
from django.core.mail import send_mail


def send_generate_old_password(email, new_password):
    send_mail(
        subject='Изменение пароля методом рандом.',
        # message=(f'Пользователь - {request.user.email}.\n'
        message=(f'Пользователь - {email}\n'
                 f'Ваш новый пароль: {new_password}'),
        from_email=settings.EMAIL_HOST_USER,
        # recipient_list=[request.user.email]
        recipient_list=[email]
    )


def send_generate_new_password(email, new_password):
    send_mail(
        subject='Восстановление пароля методом рандом.',
        message=(f'Пользователь - {email}\n'
                 f'Ваш новый пароль: {new_password}'),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
