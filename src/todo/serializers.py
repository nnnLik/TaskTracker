from rest_framework.serializers import ModelSerializer

from src.todo.models import (
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


class GlobalCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = GlobalCategory
        fields = ("id", "name",)


class UserCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = UserCategory
        fields = ("id", "user", "name",)


class TaskGlobalCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = TaskGlobalCategory
        fields = ("task", "global_category")


class TaskUserCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = TaskUserCategory
        fields = ("task", "user_category")
