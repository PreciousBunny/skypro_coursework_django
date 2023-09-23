from django.db import models
from django.urls import reverse

from users.models import User

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    """
    Класс для работы с моделью Постов.
    """
    name = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, unique=True,  verbose_name='URL')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='post/', verbose_name='Изображение', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Признак публикации', default=True)
    view_count = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)
    created_by = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, related_name='post', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """
        Класс мета-настроек.
        """
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('name', 'slug', '-creation_date',)
        permissions = [
            (
                'can_change_post',
                'Can change post'
            ),
        ]

    def increase_views(self):
        """
        Метод увеличивает количество просмотров.
        """
        self.view_count += 1
        self.save()

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

