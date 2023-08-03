from django.db import models

# Create your models here.
from django.db import models


class DEVICE(models.Model):

    device_name = models.CharField(verbose_name='设备名称',max_length=128)
    device_status = models.BooleanField(verbose_name='设备状态')

    class Meta:

        verbose_name = "设备管理"
        verbose_name_plural = "设备管理"