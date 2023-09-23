from django import template
from main.models import Client


register = template.Library()


@register.simple_tag
def active_clients_count():
    count = Client.objects.filter(is_active=True).count()
    return f'{count}'
