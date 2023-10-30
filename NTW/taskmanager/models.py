from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/taskmanager/{self.id}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'