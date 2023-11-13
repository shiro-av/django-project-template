import datetime

from django.db import models
from django.db.models import PROTECT

from users.models.users import User


class ForumPrograms(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название программы')
    description = models.TextField(verbose_name='Описание')
    page_content = models.TextField(verbose_name='Контент')
    STATUS_CHOICES = (
        ('PENDING', 'Ожидание'),
        ('PROCESS', 'В процессе'),
        ('COMPLETED', 'Завершено'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING', verbose_name='Статус заявки')
    start_date = models.DateTimeField(verbose_name='Время начала', null=True)
    end_date = models.DateTimeField(verbose_name='Время оконачния', null=True)
    owner = models.ForeignKey(User, on_delete=PROTECT, null=True)


class ForumBaseInfo(models.Model):
    # общая информация о форуме, дата, время и место проведения, реклама форума.
    title = models.CharField(max_length=100, verbose_name='Информация о форуме')
    description = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата форума')
    location = models.CharField(max_length=256, verbose_name='Место проведения')
    # advertising = models.TextField(verbose_name='Реклама')


