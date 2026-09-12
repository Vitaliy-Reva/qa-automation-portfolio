from pydantic import BaseModel, EmailStr


class Posts(BaseModel):
    id: int
    userId: int
    title: str
    body: str


class Comments(BaseModel):
    id: int
    postId: int
    name: str
    email: EmailStr
    body: str