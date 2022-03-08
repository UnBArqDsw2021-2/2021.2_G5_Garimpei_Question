from fastapi import APIRouter


router = APIRouter(
    prefix='/check',
    tags=['check']
)


@router.get('/')
def check():
    return dict(ok=True)
