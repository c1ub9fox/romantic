# Generated by Django 4.2.4 on 2023-08-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'verbose_name': '设备管理', 'verbose_name_plural': '设备管理'},
        ),
        migrations.RenameField(
            model_name='device',
            old_name='device_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='device_status',
            new_name='status',
        ),
        migrations.AddField(
            model_name='device',
            name='date',
            field=models.DateField(default=None, verbose_name='维保到期时间'),
        ),
        migrations.AddField(
            model_name='device',
            name='ip',
            field=models.GenericIPAddressField(default=None, verbose_name='设备管理地址'),
        ),
        migrations.AddField(
            model_name='device',
            name='sn',
            field=models.CharField(default=None, max_length=128, verbose_name='设备序列号'),
        ),
    ]
