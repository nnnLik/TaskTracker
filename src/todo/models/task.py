from django.db import models
from django.contrib.auth.models import User


from src.core.choices import PriorityChoices, StatusChoice
from src.core.model_fields import get_field_from_choices


class Task(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    priority = get_field_from_choices(
        "Priority", PriorityChoices, default=PriorityChoices.NORMAL
    )
    status = get_field_from_choices(
        "Status", StatusChoice, default=StatusChoice.IN_PROGRESS
    )
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
