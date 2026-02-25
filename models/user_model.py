from pydantic import BaseModel

class UserBody(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int