from typing import List, Optional
from pydantic import BaseModel


class QuestionSchema(BaseModel):
    text: str
    item_id: int
    user_id: int

    class Config():
        orm_mode = True


class AnswerSchema(BaseModel):
    text: str
    item_id: int
    user_id: int
    question_id: int

    class Config():
        orm_mode = True


class ShowQuestionSchema(BaseModel):
    id: int
    text: str
    item_id: int
    user_id: int
    answers: List[AnswerSchema] = []

    class Config():
        orm_mode = True


class ShowAnswerSchema(BaseModel):
    id: int
    text: str
    item_id: int
    user_id: int
    question_id: int
    question: ShowQuestionSchema = None

    class Config():
        orm_mode = True
