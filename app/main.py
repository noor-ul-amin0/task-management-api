from fastapi import FastAPI
from app.routers import task_router, auth_router, user_router

app = FastAPI()

app.include_router(task_router.router)
app.include_router(auth_router.router)
app.include_router(user_router.router)