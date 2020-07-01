from django.db import models

# Create your models here.
class AxfWheel(models.Model):
    img = models.CharField(max_length=1260)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_wheel'

class AxfNav(models.Model):
    img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_nav'

class AxfMustBuy(models.Model):
    img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_mustbuy'