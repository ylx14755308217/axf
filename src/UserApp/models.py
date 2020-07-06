from django.db import models

# Create your models here.

# 姓名 密码 邮箱 头像

class AxfUser(models.Model):

    name = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='icons')

    active = models.BooleanField(default=False)

    token = models.CharField(max_length=128)
    class Meta:
        db_table = 'axf_user'
