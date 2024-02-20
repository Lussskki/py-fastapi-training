if __name__ == "__main__":
    import os
    import asyncio
    from dotenv import load_dotenv
    from postgre import connect_to_database

    async def main():
        load_dotenv()  
        pool = await connect_to_database()  
        async with pool.acquire() as connection:
            result = await connection.fetch(f"SELECT * FROM {os.getenv('DB_TABLE')};")
        filtered_result = [record for record in result if record[f"{os.getenv('DB_COLUMN')}"] is not None]
        for record in filtered_result:
            print(record[f"{os.getenv('DB_COLUMN1')}"])  

    asyncio.run(main())
