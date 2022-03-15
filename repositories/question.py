from sqlalchemy.orm import Session
from schemas import QuestionSchema
from models import Question
from fastapi import status, HTTPException


def create(request: QuestionSchema, db: Session):
    text = request.text
    item_id = request.item_id
    user_id = request.user_id

    question = Question(
        text=text,
        item_id=item_id,
        user_id=user_id
    )
    db.add(question)
    db.commit()
    db.refresh(question)

    return question


def destroy(id: int, db: Session):
    question = db.query(Question).filter(Question.id == id)

    if not question.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Question with the id {id} does not exists.'
        )

    question.delete(synchronize_session=False)
    db.commit()
    return True


def update(id: int, request: QuestionSchema, db: Session):
    question = db.query(Question).filter(Question.id == id)

    if not question.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Question with the id {id} does not exists.'
        )

    question.update(request.dict())
    db.commit()
    return question.first()


def get_all_for_item(item_id: int, db: Session):
    questions = db.query(Question).filter(Question.item_id == item_id).all()
    return questions

def show(id: int, db: Session):
    question = db.query(Question).filter(Question.id == id).first()

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Question with the id {id} does not exists.'
        )
    return question
