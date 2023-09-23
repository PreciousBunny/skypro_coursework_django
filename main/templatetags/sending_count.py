from django import template
from django.conf import settings
from main.models import Sending

register = template.Library()


@register.simple_tag
def sending_count():
    count = Sending.objects.all().count()
    word = ""
    if count == 1 or (count > 20 and count % 10 == 1) \
            and count % 100 != 11:
        word = "рассылка"
    elif (1 < count < 5) or \
            (count > 20 and 1 < count % 10 < 5):
        word = "рассылки"
    elif count == 0 or (count > 1 and count < 20) \
            or count % 10 == 0 or count % 100 >= 11 \
            or count % 10 >= 5 or count % 100 >= 10:
        word = "рассылок"
    return f'{count} {word}'
