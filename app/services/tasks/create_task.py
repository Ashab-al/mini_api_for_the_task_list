
from models.task import Task
from schemas.api.tasks.create.request import TaskCreateRequest


def create_task(task: TaskCreateRequest, db: list[Task]):
    new_task = Task(
        id=len(db) + 1,
        title=task.title,
        description=task.description,
        status=task.status
    )

    db.append(new_task)

    return new_task
