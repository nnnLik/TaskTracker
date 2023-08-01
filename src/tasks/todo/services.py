import logging

from django.utils import timezone

from src.core.choices import StatusChoice, PriorityChoices
from src.notification.models import UserNotification
from src.todo.models import Task

logger = logging.getLogger(__name__)


class TodoTaskService:
    def process_task(self, task_id: int):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            logger.warning(f"Task (id: {task_id}) was deleted")
            return

        if task.status == StatusChoice.IN_PROGRESS and task.due_date <= timezone.now():
            UserNotification.objects.create(
                user=task.author,
                title=f"Task '{task.title}' is overdue!",
                body=f"The due date for task '{task.title}' has passed.",
                priority=PriorityChoices.NORMAL,
            )
            task.status = StatusChoice.DONE
            task.save()

        return


todo_task_service = TodoTaskService()
