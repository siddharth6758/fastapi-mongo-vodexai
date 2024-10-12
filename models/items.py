from pydantic import BaseModel, EmailStr, validator, Field
from datetime import datetime

class Item(BaseModel):
    name: str
    email: EmailStr
    item_name: str
    quantity: int
    expiry_date: str
    add_date: datetime = Field(default_factory=datetime.now)

    @validator('expiry_date')
    def validate_expiry_date(cls, val):
        try:
            expiry_date = datetime.strptime(val, '%d/%m/%Y')
        except ValueError:
            raise ValueError('Expiry date must be in the format dd/mm/yyyy')
        if expiry_date < datetime.now():
            raise ValueError('Expiry date must be in the future')
        return expiry_date