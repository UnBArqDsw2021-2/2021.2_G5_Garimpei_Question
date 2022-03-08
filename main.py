import uvicorn
from fastapi import FastAPI
from routers.check import router as check_router
from common.database import engine


app = FastAPI()

app.include_router(check_router)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)