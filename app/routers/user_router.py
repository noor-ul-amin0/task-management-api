from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.managers.user_manager import UserManager

router = APIRouter(prefix='/users', tags=['Users'])

user_manager = UserManager()


@router.get('/{user_id}')
def read_user(user_id: str):
    user = user_manager.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"success": True, "data": user}


@router.put('/{user_id}')
def update_user(user_id: str, user: User):
    updated_user = user_manager.update_user(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"success": True, "data": updated_user}


@router.delete('/{user_id}')
def delete_user(user_id: str):
    deleted_user = user_manager.delete_user(user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"success": True, "data": deleted_user}
