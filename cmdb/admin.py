from django.contrib import admin
from .models import DEVICE


@admin.register(DEVICE)
class device_admin(admin.ModelAdmin):
    list_display = ('name','sn','date','ip','status')
    list_per_page = 10
