from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db.models import CASCADE, PROTECT
from .groups import Groups


class User(AbstractUser):
    mobile_phone = models.CharField(max_length=20, verbose_name='Мобильный номер')
    gender = models.CharField(max_length=2, verbose_name='Пол')
    birth_date = models.DateField(default=now, verbose_name='Дата рождения')
    is_capitan = models.BooleanField(default=False, verbose_name='')
    group = models.ForeignKey(Groups, on_delete=PROTECT, null=True, verbose_name='Комманда/группа')

    def __str__(self):
        return self.username
