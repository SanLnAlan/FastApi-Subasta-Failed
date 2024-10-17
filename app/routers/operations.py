from fastapi import APIRouter

router = APIRouter(
    prefix="/operations",
)

@router.get("/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# @router.put("/{item_id}")
# def update_operation(
    
# )