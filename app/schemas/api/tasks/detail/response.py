from pydantic import BaseModel, Field, ConfigDict
from models.task import Status

class TaskDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., examples=[1])
    title: str = Field(..., examples=["Купить молоко"])
    description: str | None = Field(None, examples=["2 литра"])
    status: Status = Field(..., examples=["new"])
