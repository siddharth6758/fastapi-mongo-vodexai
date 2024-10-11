from fastapi import HTTPException

def getClockRecordFromId(record):
    if record == None:
        raise HTTPException(status_code=404, detail="Record not found")
    return {
        "id": str(record["_id"]),
        "email": record["email"],
        "location": record["location"],
        "record_date": record["record_date"]
    }

def getAllClockRecords(record_list):
    return [getClockRecordFromId(record) for record in record_list]