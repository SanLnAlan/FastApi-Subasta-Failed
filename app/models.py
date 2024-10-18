from pydantic import BaseModel, Field, PrivateAttr
from datetime import datetime
from typing import List, Optional
from enum import Enum
from uuid import UUID, uuid4


class RoleEnum(str, Enum):
    operator = "operator"
    inversor = "inversor"


class StatusEnum(str, Enum):
    open = "open"
    closed = "closed"


class User(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Unique identifier for the user",
        title="ID",
        example="3725f377-11d4-4f09-a7bf-e292ae783c11"
    )
    username: str = Field(..., description="Username of the user")
    fullname: str = Field(..., description="Fullname of the user")
    role: RoleEnum = Field(..., description="Role of the user", example="operator")


class UpdateUser(BaseModel):
    username: Optional[str] = Field(None, description="Username of the user")
    fullname: Optional[str] = Field(None, description="Fullname of the user")
    role: Optional[RoleEnum] = Field(None, description="Role of the user", example="operator")


class Operation(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Unique identifier for the operation",
        title="ID",
        example="3725f377-11d4-4f09-a7bf-e292ae783c99"
    )
    amount_required: float = Field(..., description="Amount required to be sucessfully sold")
    amount_limit: float = Field(..., description="Maximum allowable amount of money that can be invested")
    interest_rate: float = Field(
        ...,
        description="The interest rate that determines the return on investment or cost over time"
    )

    date_deadline: datetime = Field(..., title="Deadline", description="The final date by which the operation must be completed")
    datetime_published: datetime = Field(..., title="Date published", description="Date and time when the operation was created")
    # _datetime_published: datetime = PrivateAttr(Field(default_factory=datetime.now))
    status: StatusEnum = Field(StatusEnum.open, description="Status of the operation")
    bids: list[UUID] = []
    creator_user_id: UUID = Field(None, description="This field wll be auto fill.")
    inversor_user_id: UUID = Field(None, description="The user operator who won or has the best bid.")


class UpdateOperation(BaseModel):
    amount_required: float = Field(None, description="Amount required to be sucessfully sold")
    amount_limit: float = Field(None, description="Maximum allowable amount of money that can be invested")
    interest_rate: float = Field(
        None,
        description="The interest rate that determines the return on investment or cost over time"
    )
    date_deadline: datetime = Field(None, title="Deadline", description="The final date by which the operation must be completed")


class Bid(BaseModel):
    amount: float
    interest_rate: float


class Ejemplo(BaseModel):
    ejemplo: int