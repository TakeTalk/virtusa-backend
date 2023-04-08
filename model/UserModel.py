from pydantic import BaseModel
class UserBody(BaseModel):
    email: str
    phone: str | None = None
    firstName: str
    middleName: str | None = None
    lastName: str
    rewardsPoints: int


