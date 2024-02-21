import os
import asyncpg

async def connect_to_database():
    return await asyncpg.create_pool(
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_DATABASE"),
        host="localhost",
        port="5432"
    )

async def execute_query(query, *args):
    pool = await connect_to_database()  
    async with pool.acquire() as connection:
        print("Conected")
        return await connection.execute(query, *args)


"""
This code is for connect with Postgresql16 

async def main():
    result = await execute_query("SELECT * FROM table1;")
    print("connected")
    print(result)

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
"""