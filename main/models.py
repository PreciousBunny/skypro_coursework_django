from datetime import date, datetime
from django.db import models
from config.settings import AUTH_USER_MODEL

# Create your models here.


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """
    Класс для работы с моделью Клиента сервиса.
    """
    name = models.CharField(max_length=150, verbose_name='Имя', **NULLABLE)
    email = models.EmailField(max_length=150, verbose_name='Почта', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Кем создан',
                                   related_name='client', **NULLABLE)

    # поле определения активных клиентов
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса для пользователей.
        """
        return f'{self.email} ({self.name})'

    class Meta:
        """
        Класс мета-настроек.
        """
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('email',)  # сортировка, '-email' - сортировка в обратном порядке
        permissions = [
            (
                'can_view_client',
                'Can view client'
            ),
            (
                'can_block_client',
                'Can block client'
            ),
        ]


class Message(models.Model):
    """
    Класс для работы с моделью Сообщения для рассылки.
    """
    subject = models.CharField(max_length=255, verbose_name='Тема сообщения')
    body = models.TextField(verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    class Meta:
        """
        Класс мета-настроек.
        """
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса для пользователей.
        """
        return self.subject


class Sending(models.Model):
    """
    Класс для работы с моделью настройки Рассылки.
    """
    ONCE = 'Один раз'
    DAILY = '1 раз в день'
    WEEKLY = '1 раз в неделю'
    MONTHLY = '1 раз в месяц'

    FREQUENCY_CHOICES = [
        (ONCE, 'Один раз'),
        (DAILY, '1 раз в день'),
        (WEEKLY, '1 раз в неделю'),
        (MONTHLY, '1 раз в месяц'),
    ]

    CREATED = 'Создана'
    COMPLETED = 'Завершена'
    LAUNCHED = 'Запущена'

    SELECT_STATUS = [
        (CREATED, 'Создана'),
        (COMPLETED, 'Завершена'),
        (LAUNCHED, 'Запущена'),
    ]

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    scheduled_time = models.TimeField(auto_now_add=True, verbose_name='Время рассылки')
    # created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(default=date.today, verbose_name='Дата начала')
    end_date = models.DateField(default=date.today, verbose_name='Дата окончания')
    frequency = models.CharField(max_length=30, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=50, default='Создана', choices=SELECT_STATUS, verbose_name='Статус')
    created = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Кем создано',
                                related_name='clients', **NULLABLE)

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса для пользователей.
        """
        return f'ID: {self.id} - время рассылки: {self.scheduled_time}'

    class Meta:
        """
        Класс мета-настроек.
        """
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        permissions = [
            (
                'set_sending_status',
                'Can set sending status'
            ),
            (
                'can_view_sending',
                'Can view sending'
            ),
        ]


class Attempt(models.Model):
    """
    Класс для работы с моделью настройки Попытки Рассылки.
    """
    DELIVERED = 'delivered'
    NOT_DELIVERED = 'not_delivered'

    STATUS = (
        (DELIVERED, 'доставлено'),
        (NOT_DELIVERED, 'не доставлено'),
    )

    sending = models.ForeignKey(Sending, on_delete=models.CASCADE, verbose_name='Рассылка')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Время рассылки')
    status = models.CharField(choices=STATUS, verbose_name='Статус')
    response = models.TextField(**NULLABLE, verbose_name='Ответ сервера')

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса для пользователей.
        """
        return f"{self.sending.message.subject} - {self.sent_at}"

    class Meta:
        verbose_name = 'Статистика (попытка)'
        verbose_name_plural = 'Статистики (попытки)'

