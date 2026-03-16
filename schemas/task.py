from pydantic import BaseModel, Field, field_validator
import uuid                                      

class TaskCreate(BaseModel):
    titulo: str
    status: str

    @field_validator('titulo')
    @classmethod
    def ensure_title_n_empty(cls, value:str) -> str:
        if value.strip() == '':
            raise ValueError('Title cannot be empty!')
        return value
    

class Task(TaskCreate):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))

class TaskUpdate(BaseModel):
    status: str