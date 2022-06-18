from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField(verbose_name='Фото',null=True, blank=True, upload_to='news/img/')

    def __str__(self):
        return f'Новость:{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
