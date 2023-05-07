from pydantic import BaseModel,Field


class Author(BaseModel):
    id: str


class ChatModel(BaseModel):
    author: object
    createdAt: int
    id: str
    text: str
