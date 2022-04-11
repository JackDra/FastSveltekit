import os
from abc import ABC, abstractmethod

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel


class BaseRoute(ABC):

    # Used for auto template generating
    # Replace this with your data model!
    data_model = BaseModel

    def __init__(self, router: APIRouter):
        self.router = router
        self.generate_endpoints()

    def generate_endpoints(self):
        if hasattr(self, "gen_get"):
            self.get_fun = getattr(self, "gen_get")()

    @classmethod
    def generate_routes(cls, app: FastAPI, prefix: str | None = None):
        if prefix is None:
            prefix, _ = os.path.splitext(
                os.path.basename(cls.__module__.split(".")[-1])
            )
            prefix = "/" + prefix
        this_route = cls(APIRouter(prefix=prefix, tags=[prefix[1:]]))
        app.include_router(this_route.router)
        return this_route
