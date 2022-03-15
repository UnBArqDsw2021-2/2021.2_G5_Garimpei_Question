import uvicorn
from fastapi import FastAPI
from routers.check import router as check_router
from routers.answer import router as answer_router
from routers.question import router as question_router
from common.database import engine


app = FastAPI()

app.include_router(check_router)
app.include_router(answer_router)
app.include_router(question_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
