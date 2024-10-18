from fastapi import APIRouter, Path, HTTPException
from models import Operation, RoleEnum, UpdateOperation
from data.operation_dummy_data import db
from data.user_dummy_data import db as db_users
from datetime import datetime
from uuid import UUID, uuid4
# from models import User, Ejemplo

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

def verify_role(user_operator_id):
    for user in db_users:
        if user.id == user_operator_id:
            if user.role != RoleEnum.operator: 
                raise HTTPException(
                    status_code=403, detail=f"User with id {user_operator_id} does not have the operator role and cannot create operations"
                )
            break
    else:
        raise HTTPException(
                status_code=404, detail=f"User with id {user_operator_id} was not found."
            )
    return


@router.post("/{user_operator_id}")
async def create_operation(user_operator_id: UUID, operation : Operation):
    verify_role(user_operator_id)
    operation.creator_user_id = user_operator_id
    db.append(operation)
    return {"id": operation.id}


@router.put("/{operation_id}/{user_id}")
async def update_operation(operation_update: UpdateOperation, user_operator_id: UUID, operation_id: UUID):
    verify_role(user_operator_id)
    
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
    verify_role(user_operator_id)
    for operation in db:
        if operation.id == operation_id:
            db.remove(operation)
            return {"detail": "user deleted.", "user": operation}
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, id {id} not found."
    )
