from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health(): return {"status":"ok"}
@app.get("/items/{item_id}")
def read_item(item_id:int): return {"id": item_id, "name": f"item-{item_id}"}
