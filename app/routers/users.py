from fastapi import APIRouter
from models import User, UpdateUser
from data.user_dummy_data import db
from uuid import UUID
from fastapi import HTTPException
router = APIRouter(
    prefix="/users",
)

@router.get("/")
async def get_users():
    return db

# @router.get("/{id}")
# async def read_user(id: str):
#     return db_user[id]

@router.post("/")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@router.put("/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.username is not None:
                user.username = user_update
            if user_update.fullname is not None:
                user.fullname = user_update.fullname
            if user_update.role is not None:
                user.role = user_update.role
            return user.id
    raise HTTPException(
        status_code=404, detail=f"Could not find user with id {id}."
    )


@router.delete("/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"detail": "user deleted.", "user": user}
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, id {id} not found."
    )

