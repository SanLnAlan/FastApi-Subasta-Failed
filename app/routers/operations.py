from fastapi import APIRouter, Path, Body
from models import User, Ejemplo

router = APIRouter(
    prefix="/operations",
)

# @router.get("/")
# def read_operations():
#     return {db}

# def read_operation(operation_id: int):
#     return {"item_id": operation_id}

# @router.put("/{item_id}")
# def update_operation(
    
# )




# @router.post("/{operation_id}")
# async def create_operation(
#     *, #check this
#     operation_id: int = Path(
#         ...,
#         title="Id of the operation to update",
#         description="This is the description",
#         ge=0
#         ),
#     #userOperator: User,
#     amount_offered: Optional[float] = 0.0,
#     ejemplo: int = Body(...)

# ):
#     results = {"operation_id": operation_id}
#     # results.update({"user": userOperator})
#     if amount_offered:
#        results.update({"amount_offered": amount_offered})
#     # if ejemplo:
#     #     results.update({"ejemplo": ejemplo})
#     return results