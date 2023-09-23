from django.conf import settings
from django.core.mail import send_mail


def account_confirmation(obj):
    send_mail(
        subject='Подтверждение электронной почты',
        message='Добро пожаловать! Вы зарегистрировались на нашей платформе - сервисе рассылки сообщений SkyForest.\n'
        f'Для подтверждения регистрации перейдите по ссылке: http://127.0.0.1:8000/users/activate/{obj.token}\n'
        'Если вы не регистрируетесь на SkyForest, просто не обращайте внимания на это письмо.\n'
        'Скорее всего, кто-то указал вашу электронную почту по ошибке.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[obj.email],
        fail_silently=False
    )