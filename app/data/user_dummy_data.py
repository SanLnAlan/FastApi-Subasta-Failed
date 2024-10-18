from models import User
from uuid import UUID, uuid4
from typing import List

db: List[User] = [
 User(
    id="3725f377-11d4-4f09-a7bf-e292ae783c11",
    username="John",
    fullname="Doe",
    role="operator"
 ),
 User(
    id="3725f377-11d4-4f09-a7bf-e292ae783c12",
    username="Karina",
    fullname="West",
    role="inversor"
 ),
 User(
    id="3725f377-11d4-4f09-a7bf-e292ae783c13",
    username="Charles",
    fullname="Thompson",
    role="inversor"
 )
]