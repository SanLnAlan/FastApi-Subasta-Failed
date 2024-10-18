from fastapi import Path, APIRouter, HTTPException
from models import Operation, RoleEnum, UpdateOperation
from data.operation_dummy_data import db
from data.user_dummy_data import db as db_users
from datetime import datetime
from uuid import UUID, uuid4
from utils.utils import validate_role_user, validate_amounts

router = APIRouter(
    prefix="/operations",
)

@router.get("/")
async def get_operations():
    return db

@router.get("/{id}")
async def get_operation(id: UUID = Path(...,title="ID", Description="Id of the operation to retrieve")):
    for operation in db:
        if operation.id == id:
            return operation
    raise HTTPException(
        status_code=404, detail=f"Could not find operation with id {id}."
    )


@router.post("/{user_operator_id}")
async def create_operation(user_operator_id: UUID, operation : Operation):
    validate_role_user(user_operator_id, RoleEnum.operator)
    validate_amounts(operation)
    operation.creator_user_id = user_operator_id
    db.append(operation)
    return {"id": operation.id}


@router.put("/{operation_id}/{user_id}")
async def update_operation(
    operation_update: UpdateOperation,
    user_operator_id: UUID, 
    operation_id: UUID
):
    validate_role_user(user_operator_id, RoleEnum.operator)
    validate_amounts(operation_update)
    for operation in db:
        if operation.id == operation_id:
            if operation_update.amount_required:
                operation.amount_required = operation_update.amount_required
            if operation_update.amount_limit:
                operation.amount_limit = operation_update.amount_limit
            if operation_update.interest_rate:
                operation.interest_rate = operation_update.interest_rate
            if operation_update.date_deadline:
                operation.date_deadline = operation_update.date_deadline
            return {"detail": "operation updated", "operation": operation}

    raise HTTPException(
        status_code=404,
        detail=f"Operation with id {operation_id} was not found."
    )


@router.delete("/{operation_id}/{user_id}")
async def delete_operation(operation_update: UpdateOperation, user_operator_id: UUID, operation_id: UUID):
# async def delete_user(id: UUID = Path(...,title="ID", Description="Id of the user to retrieve")):
    validate_role(user_operator_id)
    for operation in db:
        if operation.id == operation_id:
            db.remove(operation)
            return {"detail": "user deleted.", "user": operation}
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, id {id} not found."
    )
