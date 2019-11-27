from django.db import models
from django.contrib.auth.models import User


class UserInfo(User):
    class Meta:
        proxy = True


class Quote(models.Model):
    quote = models.CharField(max_length=30, verbose_name='图片标签', default='', unique=True)
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    create_person = models.ForeignKey(to='userinfo.UserInfo', on_delete=models.DO_NOTHING, verbose_name='创建人')

    def __str__(self):
        return self.quote

    class Meta:
        db_table = 'quote_table'
        verbose_name = '图片标签'
        verbose_name_plural = verbose_name
