from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string


class UserInfo(User):
    class Meta:
        proxy = True


class Trade(models.Model):
    image = models.ImageField(upload_to='trade/', verbose_name='图片')
    name = models.CharField(max_length=30, verbose_name='图片说明')
    upload_time = models.DateTimeField(auto_now=True, verbose_name='上传时间')
    quote = models.ForeignKey(to='userinfo.Quote', on_delete=models.CASCADE, verbose_name='图片标签')
    user_info = models.ForeignKey(to='userinfo.UserInfo', on_delete=models.CASCADE, verbose_name='上传人')

    def __str__(self):
        return self.name

    def thumbnail(self):
        return render_to_string('image/thumb.html', {'image': self})

    def show(self):
        return render_to_string('image/show.html', {'image': self})

    thumbnail.short_description = '预览'
    show.short_description = '查看'

    class Meta:
        db_table = 'trade_table'
        verbose_name = '销售客户'
        verbose_name_plural = verbose_name


class Purchase(models.Model):
    image = models.ImageField(upload_to='purchase/', verbose_name='图片')
    name = models.CharField(max_length=30, verbose_name='图片说明')
    upload_time = models.DateTimeField(auto_now=True, verbose_name='上传时间')
    quote = models.ForeignKey(to='userinfo.Quote', on_delete=models.CASCADE, verbose_name='图片标签')
    user_info = models.ForeignKey(to='userinfo.UserInfo', on_delete=models.CASCADE, verbose_name='上传人')

    def __str__(self):
        return self.name

    def thumbnail(self):
        return render_to_string('image/thumb.html', {'image': self})

    def show(self):
        return render_to_string('image/show.html', {'image': self})

    thumbnail.short_description = '预览'
    show.short_description = '查看'

    class Meta:
        db_table = 'purchase_table'
        verbose_name = '采购客户'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    image = models.ImageField(upload_to='goods/', verbose_name='图片')
    name = models.CharField(max_length=30, verbose_name='图片说明')
    upload_time = models.DateTimeField(auto_now=True, verbose_name='上传时间')
    quote = models.ForeignKey(to='userinfo.Quote', on_delete=models.CASCADE, verbose_name='图片标签')
    user_info = models.ForeignKey(to='userinfo.UserInfo', on_delete=models.CASCADE, verbose_name='上传人')

    def __str__(self):
        return self.name

    def thumbnail(self):
        return render_to_string('image/thumb.html', {'image': self})

    def show(self):
        return render_to_string('image/show.html', {'image': self})

    thumbnail.short_description = '预览'
    show.short_description = '查看'

    class Meta:
        db_table = 'goods_table'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
