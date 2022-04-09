from typing import Any, Callable, Coroutine

from fastapi import FastAPI
from models.items import Item


def generate_item_endpoints(
    app: FastAPI,
) -> list[Callable[..., Coroutine[Any, Any, Item]]]:
    @app.get("/item", response_model=Item)
    async def create_item() -> Item:
        return Item(name="TestItem", price=5)

    return [create_item]
