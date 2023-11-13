from django.db import models


class Groups(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название комманды')
    info = models.TextField(verbose_name='Информация о комманде')