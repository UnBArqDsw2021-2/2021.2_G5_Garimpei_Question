from sqlalchemy.orm import Session
from schemas import AnswerSchema
from models import Answer, Question
from fastapi import status, HTTPException


def create(request: AnswerSchema, db: Session):
    text = request.text
    item_id = request.item_id
    user_id = request.user_id
    question_id = request.question_id
    
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Question with the id {question_id} does not exists.'
        )

    answer = Answer(
        text=text,
        item_id=item_id,
        user_id=user_id,
        question_id=question_id
    )
    db.add(answer)
    db.commit()
    db.refresh(answer)

    return answer


def destroy(id: int, db: Session):
    answer = db.query(Answer).filter(Answer.id == id)

    if not answer.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Answer with the id {id} does not exists.'
        )

    answer.delete(synchronize_session=False)
    db.commit()
    return True


def update(id: int, request: AnswerSchema, db: Session):
    answer = db.query(Answer).filter(Answer.id == id)

    if not answer.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Answer with the id {id} does not exists.'
        )

    answer.update(request.dict())
    db.commit()
    return answer.first()


def get_all_for_item(item_id: int,db: Session):
    answers = db.query(Answer).filter(Answer.item_id == item_id).all()
    return answers


def get_all_for_question(question_id: int,db: Session):
    answers = db.query(Answer).filter(Answer.question_id == question_id).all()
    return answers


def show(id: int, db: Session):
    answer = db.query(Answer).filter(Answer.id == id).first()

    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Answer with the id {id} does not exists.'
        )
    return answer
