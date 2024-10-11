from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class ClockRecords(BaseModel):
    email: EmailStr
    location: str
    record_date: datetime = Field(default_factory=datetime.now)