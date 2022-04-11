from random import randint
from typing import Any, Callable, Coroutine

from fastapi import FastAPI
from models.rand import Rand

from routes.base_route import BaseRoute


class RandRoutes(BaseRoute):

    # Used for auto template generating
    data_model = Rand

    def gen_get(self) -> Callable[[str], Coroutine[Any, Any, Rand]]:
        @self.router.get("/{rand_user}", tags=self.router.tags, response_model=Rand)
        async def create_rand(rand_user: str) -> Rand:
            return Rand(number=randint(1, 5), user=rand_user)

        # Adding this metadata allows the auto api generator
        # to generate this function
        create_rand._REST = True
        return create_rand

    def generate_endpoints(self):
        self.get_rand = self.gen_get()

    @classmethod
    def generate_routes(cls, app: FastAPI, prefix: str = "/rand"):
        return super().generate_routes(app, prefix)
