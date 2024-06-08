from fastapi import FastAPI
from pymongo import MongoClient

from controller.godsController import router as item_router

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["mars"]
collection = db["mycollection"]

app.include_router(item_router)

#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     #item_dict = God()
#     inserted_item = collection.insert_one({"hello": "world"})
#     return {"message": f"Hello {name}"}
