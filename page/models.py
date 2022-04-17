from django.db import models

# Create your models here.


class SPA(models.Model):

    data = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    name = models.CharField(max_length=100, verbose_name="Название")
    count = models.IntegerField(verbose_name="Количество", default=0)
    distance = models.IntegerField(verbose_name="Расстояние", default=0)

    def __str__(self):
        return self.name
