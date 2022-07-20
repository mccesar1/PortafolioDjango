import datetime

from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateTimeField(datetime.date.today)

    class Meta:
        verbose_name_plural='posts'
    def __str__(self):
        return (self.title)