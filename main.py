from fastapi import FastAPI
from routes.items import item
from routes.clock_in import clock

app = FastAPI()

app.include_router(item, prefix='/items')
app.include_router(clock, prefix='/clock-in')
