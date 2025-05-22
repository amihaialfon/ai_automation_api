from app.repositories.item_repository import ItemRepository
from app.models.item import Item
from app.core.logging_config import logger
class ItemService:
    def __init__(self,repo:ItemRepository):
        self._repo=repo
    def create_item(self,item:Item)->dict:
        iid,_=self._repo.create(item.dict())
        logger.info("Created item %s",iid)
        return {"id":iid,**item.dict()}
    def get_item(self,iid:int):
        logger.info("Get item %s",iid)
        return self._repo.get(iid)
    def update_item(self,iid:int,item:Item):
        logger.info("Update item %s",iid)
        return self._repo.update(iid,item.dict())
    def delete_item(self,iid:int):
        logger.info("Delete item %s",iid)
        return self._repo.delete(iid)
