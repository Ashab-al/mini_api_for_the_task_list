from models.task import Task
from query_objects.tasks.find_all_tasks import find_all_tasks


def list_tasks(db: list[Task]) -> list[Task]:
    """
    Возвращает список всех задач из хранилища.

    Args:
        db (list[Task]): In-memory хранилище задач.

    Returns:
        list[Task]: Список всех найденных задач.

    Raises:
        ValueError: Если задачи не найдены в хранилище.
    """
    tasks: list[Task] | None = find_all_tasks(db)

    if tasks is None:
        raise ValueError("Tasks not found")

    return tasks
