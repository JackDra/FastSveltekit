from typing import Any, Callable, Coroutine
from venv import create

from fastapi import APIRouter, FastAPI
from models.items import Item

from routes.base_route import BaseRoute


class ItemRoutes(BaseRoute):
    def gen_get(self) -> Callable[[str], Coroutine[Any, Any, Item]]:
        @self.router.get("/{item_id}", tags=self.router.tags, response_model=Item)
        async def create_item(item_id: str) -> Item:
            return Item(name=item_id, price=len(item_id))

        return create_item

    def generate_endpoints(self):
        self.get_item = self.gen_get()

    @classmethod
    def generate_routes(cls, app: FastAPI, prefix: str = "/item"):
        return super().generate_routes(app, prefix)
