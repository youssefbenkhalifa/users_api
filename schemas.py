from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class BookingBase(BaseModel):
    booking_ref: str

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    date_of_birth: date
    freq_flyer: Optional[str] = None
    miles_balance: Optional[int] = 0

class User(UserBase):
    id: int
    is_active: bool
    bookings: List[Booking] = []

    class Config:
        orm_mode = True
