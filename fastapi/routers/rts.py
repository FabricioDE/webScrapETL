from fastapi import APIRouter, HTTPException, status,Response
from typing import Optional, Dict, List, Any
from pymongo import MongoClient
#from utils.models import Message, messages
import uvicorn

app = APIRouter()


client = MongoClient("mongodb://localhost:27017/")
db = client["webETL"]
collection = db["scrap"]


@app.get("/scrap/", summary='GET DATA',
         description='GET all data available', response_model=dict)
async def get_records():
    #records = list(collection.find())
    #records = [{"oi": 1, "tchau": 2}]
    records = collection.find_one({"chave1": "Teste Insert"})
    return records

@app.post("/scrap/")
async def post_records(record:dict):
    records = collection.insert_one(record)
    if records.acknowledged:
        return {"id": str(records.inserted_id)}
    raise HTTPException(status_code=400, detail="Record not inserted")