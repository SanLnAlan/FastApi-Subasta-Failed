from fastapi import HTTPException
from models import RoleEnum, Bid, Operation
from data.user_dummy_data import db as db_users
from uuid import UUID, uuid4

def validate_role_user(user_operator_id: UUID, role: RoleEnum):
    for user in db_users:
        if user.id == user_operator_id:
            if user.role != role: 
                raise HTTPException(
                    status_code=403, detail=f"User with id {user_operator_id} does not have the {role} role"
                )
            break
    else:
        raise HTTPException(
                status_code=404, detail=f"User with id {user_operator_id} was not found."
            )



def validate_amounts(operation: Operation):
    if operation.amount_limit <= 0:
        raise HTTPException(
            status_code=422,
            detail="The amount limit must be greater than zero."
        )
    if operation.amount_limit < operation.amount_required:
        raise HTTPException(
            status_code=422,
            detail="The amount limit cannot be less than the amount required for the operation."
        )