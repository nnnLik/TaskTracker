from django.db import models
from django.contrib.auth.models import User

from src.core.model_fields import get_field_from_choices
from src.core.choices import PriorityChoices


class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    priority = get_field_from_choices(
        "Priority", PriorityChoices, default=PriorityChoices.NORMAL
    )
    created_at = models.DateTimeField(auto_now_add=True)
