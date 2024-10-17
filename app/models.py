from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from enum import Enum

class RoleEnum(str, Enum):
    operator = "operator"
    inversor = "inversor"

class User(BaseModel):
    username: str
    fullname: str
    role: RoleEnum

class OperationCreate(BaseModel):
    amount_requiered: float
    interest_rate: float
    deadline: datetime

class BidCreate(BaseModel):
    amount: float
    interest_rate: float

class Ejemplo(BaseModel):
    ejemplo: int