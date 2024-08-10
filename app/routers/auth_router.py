from fastapi import APIRouter, HTTPException
from app.managers.user_manager import UserManager
from app.models.auth import Login, Register

router = APIRouter(prefix='/auth', tags=['Authentication'])

user_manager = UserManager()


@router.post('/login')
def login(body: Login):
    for user in user_manager.users:
        if user.email == body.email and user.password == body.password:
            return {"success": True, "data": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@router.post('/register')
def register(user: Register):
    new_user = user_manager.add_user(user)
    return {"success": True, "data": new_user}
