from fastapi import APIRouter,HTTPException
from app.models.item import Item
from app.services.item_service import ItemService
from app.repositories.item_repository import ItemRepository

router=APIRouter()
service=ItemService(ItemRepository())

@router.get("/{item_id}")
def get_item(item_id:int):
    item=service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404,detail="Item not found")
    return {"id":item_id,**item}

@router.post("/")
def create_item(item:Item):
    return service.create_item(item)

@router.put("/{item_id}")
def update_item(item_id:int,item:Item):
    res=service.update_item(item_id,item)
    if not res:
        raise HTTPException(status_code=404,detail="Item not found")
    return {"id":item_id,**res}

@router.delete("/{item_id}")
def delete_item(item_id:int):
    res=service.delete_item(item_id)
    if not res:
        raise HTTPException(status_code=404,detail="Item not found")
    return {"status":"deleted","id":item_id}
