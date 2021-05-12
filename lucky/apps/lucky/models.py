from django.db import models

from libs.models import BaseModel


# Create your models here.

class Lottery(BaseModel):
    issue = models.CharField(verbose_name='期', max_length=32, blank=False)
    type = models.CharField(verbose_name='类型', max_length=32, blank=False)
    num = models.CharField(verbose_name='号码', max_length=128, blank=False)

    class Meta:
        verbose_name = '幸运号码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.issue, self.type)
