import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from postgre import connect_to_database  

app = FastAPI()
load_dotenv()

class Item(BaseModel):
    id: int
    names: str

# Define route to retrieve data from database
@app.get("/data")
async def get_data():
    pool = await connect_to_database()
    async with pool.acquire() as connection:
        result = await connection.fetch(f"SELECT * FROM {os.getenv('DB_TABLE')};")
    # Convert result to JSON format
    data = [dict(row) for row in result]
    return data
# Create a list to store the items (this is just for demonstration purposes)
items = []
# Define the endpoint to create a new item
@app.post("/items/")
async def create_item(item: Item):
    pool = await connect_to_database()
    async with pool.acquire() as connection:
        try:
            await connection.execute(
                f"INSERT INTO {os.getenv('DB_TABLE')} (id, {os.getenv('DB_COLUMN')}) VALUES ($1, $2)",
                item.id, item.names
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail="Failed to insert item into database")
    
    return {"message": "Item created successfully", "item": item}


# Update an existing item
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    pool = await connect_to_database()
    async with pool.acquire() as connection:
        try:
            await connection.execute(
                f"UPDATE {os.getenv('DB_TABLE')} SET {os.getenv('DB_COLUMN')} = $1 WHERE id = $2",
                item.names, item_id
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail="Failed to update item in database")
    
    return {"message": "Item updated successfully"}

# Delete an item by its ID
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    pool = await connect_to_database()
    async with pool.acquire() as connection:
        try:
            await connection.execute(
                f"DELETE FROM {os.getenv('DB_TABLE')} WHERE id = $1",
                item_id
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail="Failed to delete item from database")
    
    return {"message": "Item deleted successfully"}
