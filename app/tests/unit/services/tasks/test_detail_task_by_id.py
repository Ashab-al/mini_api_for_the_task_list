from unittest.mock import Mock, patch
from models.task import Task
from services.tasks.detail_task_by_id import detail_task_by_id


def test_detail_task_by_id_returns_task_when_found():
    mock_task = Mock(spec=Task)
    mock_task.id = 1
    mock_task.title = "Test Task"

    db = [mock_task]

    result = detail_task_by_id(1, db)

    assert result == mock_task
    assert result.id == 1
    assert result.title == "Test Task"


def test_detail_task_by_id_raises_value_error_when_not_found():
    db = []

    try:
        detail_task_by_id(999, db)
        assert False, "Ожидалось исключение ValueError"
    except ValueError as e:
        assert str(e) == "Task not found"


def test_detail_task_by_id_with_multiple_tasks_finds_correct_one():
    mock_task_1 = Mock(spec=Task, id=1, title="First Task")
    mock_task_2 = Mock(spec=Task, id=2, title="Second Task")

    db = [mock_task_1, mock_task_2]

    result = detail_task_by_id(2, db)

    assert result == mock_task_2
    assert result.id == 2
    assert result.title == "Second Task"