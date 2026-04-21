from pydantic import BaseModel, Field
from models.task import Status

class TaskCreateResponse(BaseModel):
    id: int = Field(..., examples=[1])
    title: str = Field(..., examples=["Купить молоко"])
    description: str | None = Field(None, examples=["2 литра"])
    status: Status = Field(..., examples=["new"])
