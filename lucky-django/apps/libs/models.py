from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    enable = models.BooleanField(default=True, verbose_name='是否可用')
    active = models.BooleanField(default=True, verbose_name='是否激活')

    class Meta:
        abstract = True
