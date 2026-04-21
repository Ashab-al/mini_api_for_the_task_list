from unittest.mock import Mock
from models.task import Task
from schemas.api.tasks.create.request import TaskCreateRequest
from services.tasks.create_task import create_task


def test_create_task():
    title = "Test Title"
    description = "Test Description"
    status = "new"

    request = TaskCreateRequest(
        title=title,
        description=description,
        status=status
    )

    mock_db = [
        Mock(id=1, title="Existing Task", description="Old", status="done"),
    ]

    new_task = create_task(request, mock_db)

    assert new_task.id == 2
    assert new_task.title == title
    assert new_task.description == description
    assert new_task.status == status

    assert new_task in mock_db
    assert len(mock_db) == 2