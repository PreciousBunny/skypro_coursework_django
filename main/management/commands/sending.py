from django.core.management import BaseCommand

from main.services import send_email_to_clients


# attention! execute the program with the command: > python manage.py sending

class Command(BaseCommand):
    """
    Класс запускает рассылку пользователям по команде "python manage.py sending" из командной строки.
    """

    def handle(self, *args, **options):
        send_email_to_clients()
