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
        user = self.dao.get_by_email(user_data['email'])

        if user is None:
            return "пользователя с таким email не существует"

        else:
            user_data['id'] = user.id
            password_old = user.password
            password_old_entered = generate_password_hash(user_data['password_old'])
            password_new = generate_password_hash(user_data['password_new'])
            password_new_retry = generate_password_hash(user_data['password_new_retry'])

            if password_old == password_old_entered:

                if password_new == password_new_retry:

                    if password_new != password_old:
                        user_data['password'] = password_new
                        self.dao.update_user(user_data)

                        return "Пароль изменен"

                    return "Новый пароль должен отличаться от старого"

                return "ошибка в повторении нового пароля"

            return "Не правильно введен старый пароль"

    def patch_user(self, new_data):
        return self.dao.patch_user(new_data)


    def delete(self, pk):
        self.dao.delete(pk)
