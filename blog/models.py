from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Содержание')
    image = models.ImageField(upload_to='blog/photo', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publication_indicator = models.BooleanField(verbose_name='Опубликовано')
    number_of_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}, дата публикации: {self.created_at}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']