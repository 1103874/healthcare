from django.contrib import admin
from .models import DailyHealthCheck, CheckVal

# Register your models here.

@admin.register(DailyHealthCheck)
class DailyHealthCheckAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'check1', 'check2', 'check3', 'check4', 'check5', 'check6', 'update_date', 'create_date'
    ]
    search_fields = [
        'user__username'
    ]


@admin.register(CheckVal)
class CheckValAdmin(admin.ModelAdmin):
    list_display = [
        'checking'
    ]


