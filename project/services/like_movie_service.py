from typing import Optional

from project.dao.base import BaseDAO

class LikeMovieService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao


    def create(self, user):

        new_data = {
            "movie_id": movie_id,
            "user_id": user.id
        }
        return self.dao.create(new_data)


    def delete(self, pk):

        return self.dao.delete(pk)
