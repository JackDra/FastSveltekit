from pydantic import BaseModel


class Rand(BaseModel):
    user: str
    number: int
