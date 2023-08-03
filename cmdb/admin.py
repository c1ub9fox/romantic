from django.contrib import admin
from .models import DEVICE


@admin.register(DEVICE)
class device_admin(admin.ModelAdmin):
    list_display = ('device_name','device_status')
    list_per_page = 10