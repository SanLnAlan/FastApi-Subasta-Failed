from models import User
from uuid import UUID, uuid4
from typing import List


db: List[User] = [
 User(
 id=uuid4(),
 username="John",
 fullname="Doe",
 role="operator"
 ),
 User(
 id=uuid4(),
 username="John",
 fullname="Doe",
 role="inversor"
 )
]