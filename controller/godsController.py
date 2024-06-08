from main import collection

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    #item_dict = God()
    inserted_item = collection.insert_one({"hello": "Ali"})
    return {"message": f"Hello {name}"}