from typing import Any, Callable, Coroutine

from fastapi import FastAPI
from models.items import Item


def generate_item_endpoints(
    app: FastAPI,
) -> list[Callable[[Item], Coroutine[Any, Any, Item]]]:
    @app.post("/items/", response_model=Item)
    async def create_item(item: Item) -> Item:
        return item

    return [create_item]
