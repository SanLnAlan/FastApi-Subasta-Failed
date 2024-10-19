from fastapi import APIRouter, Path, HTTPException
from models import User, UpdateUser
from data.user_dummy_data import db
from uuid import UUID
from fastapi import HTTPException
from utils.utils import valid_id


router = APIRouter(
    prefix="/users",
)

@router.get("/")
async def get_users():
    return db


@router.get("/{id}")
async def get_user(id: UUID = Path(...,title="ID", Description="Id of the user to retrieve")):
    for user in db:
        if user.id == id:
            return user
    raise HTTPException(
        status_code=404, detail=f"Could not find user with id {id}."
    )


@router.post("/")
async def create_user(user: User):
    valid_id(user.id, db)
    db.append(user)
    return {"id": user.id}


@router.put("/{id}")
async def update_user(user_update: UpdateUser, id: UUID = Path(...,title="ID", Description="Id of the user to retrieve")):
    for user in db:
        if user.id == id:
            if user_update.username:
                user.username = user_update.username
            if user_update.fullname:
                user.fullname = user_update.fullname
            if user_update.role:
                user.role = user_update.role
            return {"detail": "user updated", "user": user}
    raise HTTPException(
        status_code=404, detail=f"Could not find user with id {id}."
    )


@router.delete("/{id}")
async def delete_user(id: UUID = Path(...,title="ID", Description="Id of the user to retrieve")):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"detail": "user deleted.", "user": user}
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, id {id} not found."
    )

