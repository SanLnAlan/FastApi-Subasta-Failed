from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class OperationCreate(BaseModel):
    amount_requiered: float
    interest_rate: float
    deadline: datetime

class BidCreate(BaseModel):
    amount: float
    interest_rate: float

