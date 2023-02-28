from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_password_hash


class UserService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao


    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self, page: Optional[int] = None) -> list[User]:
        return self.dao.get_all(page=page)

    def create(self, user_data):
        user_data['password'] = generate_password_hash(user_data['password'])
        return self.dao.create(user_data)

    def update(self, user_data):
        user_data['password'] = generate_password_hash(user_data['password'])
        self.dao.update_user(user_data)
        return self.dao

    def patch_user(self, user_data):
        self.dao.patch_user(user_data)
        return self.dao
    def delete(self, pk):
        self.dao.delete(pk)
