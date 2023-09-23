from django import template
from main.models import Sending
register = template.Library()

@register.simple_tag
def active_sending_count():
    send_count = Sending.objects.filter(status=Sending.LAUNCHED).count()
    word = ""
    if send_count == 1 or (send_count > 20 and send_count % 10 == 1) \
            and send_count % 100 != 11:
        word = "рассылка"
    elif (1 < send_count < 5) or \
            (send_count > 20 and 1 < send_count % 10 < 5):
        word = "рассылки"
    elif send_count == 0 or (send_count > 1 and send_count < 20) \
            or send_count % 10 == 0 or send_count % 100 >= 11 \
            or send_count % 10 >= 5 or send_count % 100 >= 10:
        word = "рассылок"
    return f'{send_count} {word}'
