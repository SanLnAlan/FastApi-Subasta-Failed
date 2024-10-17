from fastapi import APIRouter
from api import api
from models import UserCreate

router = APIRouter(
    prefix="/users",
)

@router.get("/")
async def read_users():
    return api.read_users()

@router.get("/{id}")
async def read_user(id: int):
    return api.read_user(id)

@router.post("/")
async def create_user(user: UserCreate):
    return {"message": "user created", "user": user}

# @router.post("/")
# def test():
#     return{"msg": dir(models)} 