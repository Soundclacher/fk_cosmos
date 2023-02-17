from django.db import models

# Create your models here.
class Articles(models.Model):
    image = models.ImageField('Изображение', upload_to='newsimg/')
    title = models.CharField('Заголовок', max_length=50)
    lead = models.CharField('Анонс', max_length=200)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
