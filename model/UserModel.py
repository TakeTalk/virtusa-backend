from pydantic import BaseModel
class UserBody(BaseModel):
    email: str
    phone: str
    firstName: str
    middleName: str | None = None
    lastName: str
    rewardsPoints: int

class SignIn(BaseModel):
    email: str