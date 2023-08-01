from celery import shared_task

from .services import todo_task_service


@shared_task
def process_task_due_date(task_id: int) -> None:
    return todo_task_service.process_task(task_id)


@shared_task
def sum():
    return 1 + 1
