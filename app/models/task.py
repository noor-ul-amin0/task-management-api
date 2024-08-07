from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    completed: bool = False
    created_at: Optional[str] = None
    updated_at: Optional[str] = None