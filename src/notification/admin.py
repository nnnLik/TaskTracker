from django.contrib import admin

from .models import UserNotification


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "body",
        "priority",
        "created_at",
    )
    list_filter = (
        "user",
        "priority",
        "created_at",
    )
