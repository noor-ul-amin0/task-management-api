from typing import List, Optional

from app.models.auth import Register
from app.models.user import User
from app.utils.utils import generate_id


class UserManager:
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, user: Register) -> User:
        user = User(id=generate_id(), email=user.email, password=user.password)
        self.users.append(user)
        return user

    def get_user(self, user_id: str) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update_user(self, user_id: str, updated_user: User) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                user.email = updated_user.email
                user.password = updated_user.password
                return user
        return None

    def delete_user(self, user_id: str) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                return user
        return None
