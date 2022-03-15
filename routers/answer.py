from fastapi import APIRouter
from typing import List
from schemas import AnswerSchema, ShowAnswerSchema
from fastapi import status, Depends, Response
from sqlalchemy.orm import Session
from repositories import answer as answer_repository
from common.utils import get_db



router = APIRouter(
    prefix='/answers',
    tags=['answers']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
    request: AnswerSchema,
    db: Session = Depends(get_db)
):
    return answer_repository.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id,
    db: Session = Depends(get_db)
):
    return answer_repository.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(
    id,
    request: AnswerSchema,
    db: Session = Depends(get_db)
):
    return answer_repository.update(id, request, db)


@router.get('/item/{item_id}', response_model=List[ShowAnswerSchema])
def get_all_for_item(
    item_id,
    db: Session = Depends(get_db)
):
    return answer_repository.get_all_for_item(item_id, db)


@router.get('/question/{question_id}', response_model=List[ShowAnswerSchema])
def get_all_for_item(
    question_id,
    db: Session = Depends(get_db)
):
    return answer_repository.get_all_for_item(question_id, db)


@router.get('/{id}', response_model=ShowAnswerSchema)
def show(
    id: int,
    response: Response,
    db: Session = Depends(get_db)
):
    return answer_repository.show(id, db)