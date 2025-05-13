from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answer import answer_schema, answer_crud
from domain.question import question_crud

router = APIRouter(
    prefix="/api/answer",
)

# 출력은 response_model을 사용하는 대신 status_code=status.HTTP_204_NO_CONTENT 를 사용했다. 이렇게 리턴할 응답이 없을 경우에는 응답코드 204를 리턴하여 "응답 없음"을 나타낼 수 있다.
@router.post("/create/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id: int,
                  _answer_create: answer_schema.AnswerCreate,
                  db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="질문이 존재하지 않습니다.")
    answer_crud.create_answer(db, question, _answer_create)
