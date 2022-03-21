from common.models import BaseModel
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Question(BaseModel):
    __tablename__ = "question"

    text = Column(String)
    item_id = Column(Integer)
    user_id = Column(Integer)
    answers = relationship("Answer", back_populates="question")


class Answer(BaseModel):
    __tablename__ = "answer"

    text = Column(String)
    item_id = Column(Integer)
    user_id = Column(Integer)
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship("Question", back_populates="answers")
