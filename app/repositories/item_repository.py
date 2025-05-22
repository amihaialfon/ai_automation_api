from typing import Dict,Tuple,Optional
class ItemRepository:
    def __init__(self):
        self._db:Dict[int,dict]={}
        self._id=1
    def create(self,item:dict)->Tuple[int,dict]:
        iid=self._id
        self._db[iid]=item
        self._id+=1
        return iid,item
    def get(self,iid:int)->Optional[dict]:
        return self._db.get(iid)
    def update(self,iid:int,item:dict)->Optional[dict]:
        if iid in self._db:
            self._db[iid]=item
            return item
        return None
    def delete(self,iid:int)->Optional[dict]:
        return self._db.pop(iid,None)
