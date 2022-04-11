from abc import ABC, abstractmethod

from fastapi import APIRouter, FastAPI


class BaseRoute(ABC):
    def __init__(self, router: APIRouter):
        self.router = router
        self.generate_endpoints()

    @abstractmethod
    def generate_endpoints(self):
        pass

    @classmethod
    def generate_routes(cls, app: FastAPI, prefix: str):
        this_route = cls(APIRouter(prefix=prefix))
        app.include_router(this_route.router)
        return this_route