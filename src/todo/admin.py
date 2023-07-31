from django.contrib import admin

from .models.task import Task
from .models.other import (
    GlobalCategory,
    UserCategory,
    TaskGlobalCategory,
    TaskUserCategory,
)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "description",
        "priority",
        "due_date",
        "created_at",
    )
    list_filter = (
        "priority",
        "author",
        "created_at",
    )


@admin.register(GlobalCategory)
class GlobalCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(UserCategory)
class UserCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "name",
    )
    list_filter = ("user",)


@admin.register(TaskGlobalCategory)
class TaskGlobalCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "task",
        "global_category",
    )
    list_filter = (
        "task",
        "global_category",
    )


@admin.register(TaskUserCategory)
class TaskUserCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "task",
        "user_category",
    )
    list_filter = (
        "task",
        "user_category",
    )
