from django.db import models
from django.db.models import F


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    content = models.TextField(blank=True, verbose_name="Содержание")
    image = models.ImageField(
        upload_to="blog/photo", verbose_name="Изображение", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication_indicator = models.BooleanField(
        default=False, verbose_name="Опубликовано"
    )
    number_of_views = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def increment_views(self):
        """
        Атомарно увеличивает счетчик просмотров.
        Безопасно при параллельных запросах.
        """
        self.number_of_views = F("number_of_views") + 1
        self.save(update_fields=["number_of_views"])
        self.refresh_from_db(fields=["number_of_views"])
        return self.number_of_views

    def __str__(self):
        return f"{self.title}, дата публикации: {self.created_at}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]
