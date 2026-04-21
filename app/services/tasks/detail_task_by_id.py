from models.task import Task
from query_objects.tasks.find_task_by_id import find_task_by_id


def detail_task_by_id(id: int, db: list[Task]) -> Task:
    task: Task | None = find_task_by_id(id, db)

    if task is None:
        raise ValueError("Task not found")

    return task
