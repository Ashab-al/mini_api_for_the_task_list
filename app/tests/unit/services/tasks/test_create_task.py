from unittest.mock import Mock
from models.task import Task
from schemas.api.tasks.create.request import TaskCreateRequest
from services.tasks.create_task import create_task


def test_create_task():
    # Arrange
    title = "Test Title"
    description = "Test Description"
    status = "new"

    request = TaskCreateRequest(
        title=title,
        description=description,
        status=status
    )

    # Имитируем базу данных как список задач
    mock_db = [
        Mock(id=1, title="Existing Task", description="Old", status="done"),
    ]

    # Act
    new_task = create_task(request, mock_db)

    # Assert
    assert new_task.id == 2
    assert new_task.title == title
    assert new_task.description == description
    assert new_task.status == status

    # Проверяем, что задача добавлена в БД
    assert new_task in mock_db
    assert len(mock_db) == 2