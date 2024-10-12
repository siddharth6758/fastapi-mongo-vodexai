from fastapi import APIRouter, HTTPException
from config.database import conn
from models.clock_in import ClockRecords
from schemas.clock_in import *
from bson import ObjectId
from typing import Optional
from datetime import datetime

clock = APIRouter()

@clock.post('')
async def insert_record(record: ClockRecords):
    conn.vodexai.clockrecord.insert_one(dict(record))
    return {"status": "Clock Record created", "item":str(record)}

@clock.get('/{id}')
async def get_records_from_id(id):
    try:
        item = conn.vodexai.clockrecord.find_one({'_id': ObjectId(id)})
        return getClockRecordFromId(item)
    except Exception as e:
        return HTTPException(status_code=404, detail=str(e))


@clock.get("/filter/")
async def filter_clock_records(
    email: Optional[str] = None,
    location: Optional[str] = None,
    insert_date: Optional[datetime] = None
):
    try:
        query = {}
        if email:
            query["email"] = email
        if location:
            query["location"] = location
        if insert_date:
            query["insert_date"] = {"$gt": insert_date}
        records = list(conn.vodexai.clockrecord.find(query))
        for record in records:
            record['_id'] = str(record['_id'])
        return records
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@clock.get('/')
async def get_all_records():
    records = list(conn.vodexai.clockrecord.find())
    return getAllClockRecords(records)

@clock.put('/{id}')
async def update_clock_record(id, record: ClockRecords):
    conn.vodexai.clockrecord.find_one_and_update({"_id": ObjectId(id)},{"$set":dict(record)})
    return {"status":"Clock Record Updated","record":str(record)}

@clock.delete('/{id}')
async def delete_clock_record(id):
    conn.vodexai.clockrecord.find_one_and_delete({'_id': ObjectId(id)})
    return {"status":"Clock Record Deleted"}