from pydantic import BaseModel


class UserOrganStatus(BaseModel):
    email: str
    brain: bool | None = False
    heart: bool | None = False
    lungs: bool | None = False
    liver: bool | None = False
    kidney: bool | None = False
    ortho: bool | None = False

