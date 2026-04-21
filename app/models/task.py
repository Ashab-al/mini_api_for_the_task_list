from pydantic import BaseModel, Field
from enum import Enum

class Status(str, Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task(BaseModel):
    id: int = Field(..., examples=[1])
    title: str = Field(..., examples=["Купить молоко"])
    description: str | None = Field(None, examples=["2 литра"])
    status: Status = Field(..., examples=["new"])
