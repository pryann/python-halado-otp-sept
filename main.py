from fastapi import FastAPI

app = FastAPI()

items = [
    {"id": 1, "name": "item1", "price": 10.5},
    {"id": 2, "name": "item2", "price": 20.5},
    {"id": 3, "name": "item3", "price": 30.5},
    {"id": 4, "name": "item4", "price": 40.5},
]


@app.get("/")
def read_root():
    return {"message": "API works!"}


@app.get("/items")
def get_items():
    return {"items": items}


@app.get("/items/{item_id}")
def find_item(item_id: int):
    item = next((item for item in items if item["id"] == item_id), None)
    return {"item": item}
    # item = list(filter(lambda item: item["id"] == item_id, items))
    # return {"item": item[0] if item else None}
