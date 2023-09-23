# Generated by Django 4.2.4 on 2023-09-19 01:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, max_length=150, null=True, verbose_name='Почта')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('email',),
                'permissions': [('can_view_client', 'Can view client'), ('can_block_client', 'Can block client')],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема сообщения')),
                ('body', models.TextField(verbose_name='Текст сообщения')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Sending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_time', models.TimeField(auto_now_add=True, verbose_name='Время рассылки')),
                ('start_date', models.DateField(default=datetime.date.today, verbose_name='Дата начала')),
                ('end_date', models.DateField(default=datetime.date.today, verbose_name='Дата окончания')),
                ('frequency', models.CharField(choices=[('Один раз', 'Один раз'), ('1 раз в день', '1 раз в день'), ('1 раз в неделю', '1 раз в неделю'), ('1 раз в месяц', '1 раз в месяц')], max_length=30, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('Создана', 'Создана'), ('Завершена', 'Завершена'), ('Запущена', 'Запущена')], default='Создана', max_length=50, verbose_name='Статус')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'permissions': [('set_sending_status', 'Can set sending status'), ('can_view_sending', 'Can view sending')],
            },
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True, verbose_name='Время рассылки')),
                ('status', models.CharField(choices=[('delivered', 'доставлено'), ('not_delivered', 'не доставлено')], verbose_name='Статус')),
                ('response', models.TextField(blank=True, null=True, verbose_name='Ответ сервера')),
                ('sending', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sending', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Статистика (попытка)',
                'verbose_name_plural': 'Статистики (попытки)',
            },
        ),
    ]
