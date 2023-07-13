from django.db import models

# class Img(models.Model):
#     title = models.CharField('Назва', max_length=50)
#     img = models.ImageField(upload_to='images')
#
#     def __str__(self):
#         return self.title


class Img(models.Model):
    title = models.CharField(max_length= 255)
    # , blank=False, null=False)
    image = models.ImageField(upload_to='img/', null=True, max_length=255)

    def __repr__(self):
        return 'Img(%s, %s)' % (self.title, self.image)

    def __str__ (self):
        return self.title