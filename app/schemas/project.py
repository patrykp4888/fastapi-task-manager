from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class ProjectBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class ProjectCreate(ProjectBase):
    title: str


class ProjectUpdate(ProjectBase):
    pass


class ProjectInDBBase(ProjectBase):
    id: int
    title: str
    created_at: datetime
    owner_id: int

    class Config:
        orm_mode = True
