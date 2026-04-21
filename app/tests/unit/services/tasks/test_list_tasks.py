from unittest.mock import Mock
from models.task import Task
from services.tasks.list_tasks import list_tasks


def test_list_tasks_returns_all_tasks():
    mock_task_1 = Mock(spec=Task, id=1, title="Task 1", status="new")
    mock_task_2 = Mock(spec=Task, id=2, title="Task 2", status="in_progress")

    db = [mock_task_1, mock_task_2]

    result = list_tasks(db)

    assert result == db
    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 2


def test_list_tasks_raises_when_no_tasks_found():
    db = None

    try:
        list_tasks(db)
        assert False, "Ожидалось исключение ValueError"
    except ValueError as e:
        assert str(e) == "Tasks not found"