from typing import Any, Callable, Coroutine

from fastapi import FastAPI
from models.items import Item


def generate_item_endpoints(
    app: FastAPI,
) -> list[Callable[..., Coroutine[Any, Any, Item]]]:
    @app.get("/item/{item_id}", response_model=Item)
    async def create_item(item_id: str) -> Item:
        return Item(name=item_id, price=len(item_id))

    return [create_item]
