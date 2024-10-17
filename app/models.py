from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from enum import Enum
from uuid import UUID, uuid4


class RoleEnum(str, Enum):
    operator = "operator"
    inversor = "inversor"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    username: str
    fullname: str
    role: RoleEnum

class UpdateUser(BaseModel):
    username: Optional[str]
    fullname: Optional[str]
    role: Optional[RoleEnum]

class OperationCreate(BaseModel):
    amount_requiered: float
    interest_rate: float
    deadline: datetime

class BidCreate(BaseModel):
    amount: float
    interest_rate: float

class Ejemplo(BaseModel):
    ejemplo: int