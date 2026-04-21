from models.task import Task

def find_task_by_id(id: int, db: list[Task]) -> Task | None:
    for task in db:
        if task.id == id:
            return task

    return None
