from django.db import models

# Create your models here.
from django.db import models


class DEVICE(models.Model):

    sn = models.CharField(verbose_name="设备序列号",max_length=128,default=None)
    name = models.CharField(verbose_name='设备名称',max_length=128)
    ip = models.GenericIPAddressField(verbose_name="设备管理地址",default=None)
    date = models.DateField(verbose_name="维保到期时间",default=None)
    status = models.BooleanField(verbose_name='设备状态')

    class Meta:

        verbose_name = "设备管理"
        verbose_name_plural = "设备管理"