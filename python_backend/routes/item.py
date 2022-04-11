from typing import Any, Callable, Coroutine

from fastapi import FastAPI
from models.item import Item

from routes.base_route import BaseRoute


class ItemRoutes(BaseRoute):

    # Used for auto template generating
    data_model = Item

    def gen_get(self) -> Callable[[str], Coroutine[Any, Any, Item]]:
        @self.router.get("/{item_id}", tags=self.router.tags, response_model=Item)
        async def create_item(item_id: str) -> Item:
            return Item(name=item_id, price=len(item_id))

        # Adding this metadata allows the auto api generator
        # to generate this function
        create_item._REST = True
        return create_item
