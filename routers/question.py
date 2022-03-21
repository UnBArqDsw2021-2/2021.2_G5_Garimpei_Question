from fastapi import APIRouter
from typing import List
from schemas import QuestionSchema, ShowQuestionSchema
from fastapi import status, Depends, Response
from sqlalchemy.orm import Session
from repositories import question as question_repository
from common.utils import get_db



router = APIRouter(
    prefix='/questions',
    tags=['questions']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
    request: QuestionSchema,
    db: Session = Depends(get_db)
):
    return question_repository.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id,
    db: Session = Depends(get_db)
):
    return question_repository.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(
    id,
    request: QuestionSchema,
    db: Session = Depends(get_db)
):
    return question_repository.update(id, request, db)


@router.get('/item/{item_id}', response_model=List[ShowQuestionSchema])
def get_all_for_item(
    item_id,
    db: Session = Depends(get_db)
):
    return question_repository.get_all_for_item(item_id, db)


@router.get('/{id}', response_model=ShowQuestionSchema)
def show(
    id: int,
    response: Response,
    db: Session = Depends(get_db)
):
    return question_repository.show(id, db)