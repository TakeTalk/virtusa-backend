from pydantic import BaseModel


class UserBody(BaseModel):
    email: str
    phone: str | None = None
    name: str
    photoUrl: str
    rewardsPoints: int
    location_lat: str
    location_long: str
    medicine: bool
    insurance: bool
