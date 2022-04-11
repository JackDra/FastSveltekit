from random import randint
from typing import Any, Callable, Coroutine

from fastapi import FastAPI
from models.rand import Rand

from routes.base_route import BaseRoute


class RandRoutes(BaseRoute):

    # Used for auto template generating
    data_model = Rand

    # gen_ and then the REST call (get, post, etc..) will be
    # recognized by the auto doc generator
    def gen_get(self) -> Callable[[str], Coroutine[Any, Any, Rand]]:
        @self.router.get("/{rand_user}", tags=self.router.tags, response_model=Rand)
        async def create_rand(rand_user: str) -> Rand:
            return Rand(number=randint(1, 5), user=rand_user)

        # Adding this metadata allows the auto api generator
        # to generate this function
        create_rand._REST = True
        return create_rand
