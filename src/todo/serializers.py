from dateutil.parser import isoparse
from datetime import datetime, timezone

from rest_framework.serializers import ModelSerializer

from src.tasks.todo.tasks import process_task_due_date

from .models import (
    Task,
    GlobalCategory,
    UserCategory,
    TaskGlobalCategory,
    TaskUserCategory,
)


class TaskModelSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "author",
            "description",
            "priority",
            "status",
            "due_date",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        due_date = validated_data.get("due_date")
        time_difference = due_date - datetime.now(timezone.utc)
        countdown = int(time_difference.total_seconds())

        task = Task.objects.create(**validated_data)

        process_task_due_date.apply_async(args=[task.id], countdown=countdown)

        return task


class GlobalCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = GlobalCategory
        fields = (
            "id",
            "name",
        )


class UserCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = UserCategory
        fields = (
            "id",
            "user",
            "name",
        )


class TaskGlobalCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = TaskGlobalCategory
        fields = ("task", "global_category")


class TaskUserCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = TaskUserCategory
        fields = ("task", "user_category")
