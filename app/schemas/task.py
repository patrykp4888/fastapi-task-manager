from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from app.models.task import TaskStatus, TaskPriority


class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None


class TaskCreate(TaskBase):
    title: str
    project_id: int


class TaskUpdate(TaskBase):
    project_id: Optional[int] = None
    assignee_id: Optional[int] = None


class TaskInDBBase(TaskBase):
    id: int
    title: str
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    project_id: int
    assignee_id: Optional[int]

    class Config:
        orm_mode = True
