from fastapi import APIRouter, Path, HTTPException
from models import RoleEnum, Bid
from data.bid_dummy_data import db
from data.user_dummy_data import db as db_users
from datetime import datetime
from uuid import UUID, uuid4
from utils.utils import validate_role_user, validate_id_operation, validate_amount_offered, valid_id, update_winning_bids

router = APIRouter(
    prefix="/bids",
)

@router.get("/")
async def get_bids():
    return db

@router.get("/{id}")
async def get_bid(id: UUID = Path(...,title="ID", Description="Id of the bid to retrieve")):
    for bid in db:
        if bid.id == id:
            return bid
    raise HTTPException(
        status_code=404, detail=f"Could not find bid with id {id}."
    )


@router.post("/{user_inversor_id}")
async def create_bid(user_inversor_id: UUID, bid : Bid):
    valid_id(bid.id, db)
    validate_role_user(user_inversor_id, RoleEnum.inversor)
    validate_id_operation(bid.operation_id)
    validate_amount_offered(bid, bid.operation_id)
    bid.created_at = datetime.now()
    bid.updated_at = datetime.now()
    bid.creator_user_id = user_inversor_id
    bid.is_winning = True
    update_winning_bids(bid.id, bid.operation_id)
    db.append(bid)
    return {"id": bid.id}


# @router.put("/{operation_id}/{user_id}")
# async def update_operation(
#     operation_update: UpdateBid,
#     user_operator_id: UUID, 
#     operation_id: UUID
# ):
#     validate_role(user_operator_id)
#     validate_amounts(operation_update)
#     for operation in db:
#         if operation.id == operation_id:
#             if operation_update.amount_required:
#                 operation.amount_required = operation_update.amount_required
#             if operation_update.amount_limit:
#                 operation.amount_limit = operation_update.amount_limit
#             if operation_update.interest_rate:
#                 operation.interest_rate = operation_update.interest_rate
#             if operation_update.date_deadline:
#                 operation.date_deadline = operation_update.date_deadline
#             return {"detail": "operation updated", "operation": operation}

#     raise HTTPException(
#         status_code=404,
#         detail=f"Operation with id {operation_id} was not found."
#     )


# @router.delete("/{operation_id}/{user_id}")
# async def delete_operation(operation_update: UpdateOperation, user_operator_id: UUID, operation_id: UUID):
# # async def delete_user(id: UUID = Path(...,title="ID", Description="Id of the user to retrieve")):
#     validate_role(user_operator_id)
#     for operation in db:
#         if operation.id == operation_id:
#             db.remove(operation)
#             return {"detail": "user deleted.", "user": operation}
#     raise HTTPException(
#         status_code=404, detail=f"Delete user failed, id {id} not found."
#     )
