import datetime
from fastapi import HTTPException
from starlette import status
from pydantic import BaseModel, field_validator

class AnswerCreate(BaseModel):
    content: str

    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
            #raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='빈 값은 허용되지 않습니다.')
        return v
    
class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
