from django.db import models


class BaseTextChoices(models.TextChoices):
    @classmethod
    def max_length(cls):
        return max([len(v) for v in cls.values])


class PriorityChoices(BaseTextChoices):
    LOW = "LOW", "Low"
    NORMAL = "NORMAL", "Normal"
    HIGH = "HIGH", "High"


class StatusChoice(BaseTextChoices):
    OPEN = "OPEN", "Open"
    IN_PROGRESS = "IN_PROGRESS", "In Progress"
    DONE = "DONE", "Done"
