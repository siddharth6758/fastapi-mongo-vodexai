from fastapi import APIRouter, HTTPException
from config.database import conn
from models.items import Item
from schemas.items import *
from bson import ObjectId
from typing import Optional, List, Dict

item = APIRouter()

@item.post('/items')
async def insert_item(item: Item):
    conn.vodexai.items.insert_one(dict(item))
    return {"status": "Item created", "item":str(item)}

@item.get('/items/{id}')
async def get_item_from_id(id):
    try:
        item = conn.vodexai.items.find_one({'_id': ObjectId(id)})
        return getItemFromId(item)
    except Exception as e:
        return HTTPException(status_code=404, detail=str(e))


@item.get("/items/filter")
async def filter_items(
    email: Optional[str] = None,
    expiry_date: Optional[datetime] = None,
    insert_date: Optional[datetime] = None,
    quantity: Optional[int] = None
):
    try:
        query = {}
        if email:
            query["email"] = email
        if expiry_date:
            query["expiry_date"] = {"$gt": expiry_date}
        if insert_date:
            query["insert_date"] = {"$gt": insert_date}
        if quantity is not None:
            query["quantity"] = {"$gte": quantity}
        items = []
        async for item in conn.vodexai.items.find(query):
            item["id"] = str(item["_id"])
            items.append(item)
        return items
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@item.get('/')
async def get_all_items():
    items = list(conn.vodexai.items.find())
    return getAllItems(items)

@item.put('/items/{id}')
async def update_item(id, item: Item):
    conn.vodexai.items.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(item)})
    return {"status":"Item Updated","item":str(item)}

@item.delete('/items/{id}')
async def delete_item(id):
    conn.vodexai.items.find_one_and_delete({'_id': ObjectId(id)})
    return {"status":"Item Deleted"}