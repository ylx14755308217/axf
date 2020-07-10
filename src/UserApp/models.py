from django.db import models

# Create your models here.
# 姓名   密码   邮箱  头像  (active token)

class AxfUser(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='icons')

    # 注册账户的时候 默认情况下是非激活状态
    active = models.BooleanField(default=False)

    token = models.CharField(max_length=128)

    class Meta:
        db_table = 'axf_user'
