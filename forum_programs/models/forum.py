import datetime
from django.db import models
from django.db.models import PROTECT
from users.models.users import User


class ForumBaseInfo(models.Model):
    # общая информация о форуме, дата, время и место проведения, реклама форума.
    title = models.CharField(max_length=100, verbose_name='Информация о форуме')
    description = models.TextField(verbose_name='Описание')
    short_description = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата форума')
    location = models.CharField(max_length=256, verbose_name='Место проведения')
    owner = models.ForeignKey(User, on_delete=PROTECT, null=True)
    # advertising = models.TextField(verbose_name='Реклама')


# schedule
class ForumProgramItem(models.Model):
    Forum = models.ForeignKey(ForumBaseInfo, on_delete=PROTECT, verbose_name='Форум')
    title = models.CharField(max_length=100, verbose_name='Название программы')
    description = models.TextField(verbose_name='Описание')
    start_time = models.TimeField(auto_now=False, blank=True, verbose_name='Время начала')
    end_time = models.TimeField(auto_now=False, blank=True, verbose_name='Время окончания')
    date = models.DateField(default=datetime.date(23, 11, 1), verbose_name='Дата')





