from fastapi import HTTPException
from models import RoleEnum, Bid, Operation
from data.user_dummy_data import db as db_users
from data.bid_dummy_data import db as db_bid
from data.operation_dummy_data import db as db_operation
from uuid import UUID, uuid4

def valid_id(id: UUID, db):
    for item in db:
        if id == item.id:
            raise HTTPException(
                    status_code=400, detail=f"ID already exists."
                )

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
            detail="The amount limit cannot be less than the required amount for the operation."
        )
    
def validate_id_operation(id: UUID):
    for operation in db_operation:
        if operation.id == id:
            break
    else:
        raise HTTPException(
                status_code=404, detail=f"Operation with id {id} was not found."
            )

def validate_amount_offered(bid: Bid, operation_id):
    for operation in db_operation:
        if operation.id == operation_id:
            if bid.amount_offered < operation.amount_required:
                raise HTTPException(
                    status_code=400, detail=f"Amount offered is fewer than required amount."
                )
            if operation.amount_current:
                if bid.amount_offered <= operation.amount_current:
                    raise HTTPException(
                        status_code=400, detail=f"Amount offered is fewer or equal than current amount."
                    )
            operation.amount_current = bid.amount_offered
            if bid.id not in operation.bids:
                operation.bids.append(bid.id)
            break

def update_winning_bids(bid_id_winner, operation_id):
    for operation in db_operation:
        if operation_id == operation.id:
            bids_in_operation = operation.bids
            operation.bids.append(operation_id)
    print("bids_in_operation: ", bids_in_operation)
    for bid in db_bid:
        if bid.id in bids_in_operation:
            print("bid to be change: ", bid.id)
            bid.is_winning = False
