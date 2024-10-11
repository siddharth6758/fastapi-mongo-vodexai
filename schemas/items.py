from typing import Optional
from fastapi import HTTPException
from datetime import datetime

def getItemFromId(item):
    if item == None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "item_name": item["item_name"],
        "quantity": item["quantity"],
        "expiry_date": item["expiry_date"],
        "add_date": item["add_date"]
    }

def getAllItems(items_list):
    return [getItemFromId(item) for item in items_list]