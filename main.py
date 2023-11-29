from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine, MetaData, Table, select
from databases import Database

DATABASE_URL = "mysql+mysqlconnector://user:password@localhost:3306/mydatabase"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    query = f"SELECT * FROM items WHERE id = {item_id}"
    result = await database.fetch_one(query)
    return result