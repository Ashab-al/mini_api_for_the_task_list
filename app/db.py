from models.task import Task


database: list[Task] = []
"""
In-memory база данных задач.

Description:
    Хранит список задач в виде объектов модели Task (Pydantic).
    Используется как временное хранилище в памяти приложения.

Structure:
    list[Task]: список объектов Task
"""