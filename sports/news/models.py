from django.db import models
class Articles(models.Model):
    tittle = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст')
    data_time = models.DateTimeField('Дата')

    def __str__(self):
        return self.tittle

