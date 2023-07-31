from django.db import models
from django.contrib.auth.models import User

from src.todo.models.task import Task


class GlobalCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "global_category"


class UserCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "user_category"


class TaskGlobalCategory(models.Model):
    global_category = models.ForeignKey(GlobalCategory, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        db_table = "task_global_category"


class TaskUserCategory(models.Model):
    user_category = models.ForeignKey(UserCategory, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        db_table = "task_user_category"
