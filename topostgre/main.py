if __name__ == "__main__":
    import asyncio
    from dotenv import load_dotenv
    from postgre import connect_to_database

    async def main():
        load_dotenv()  
        pool = await connect_to_database()  
        async with pool.acquire() as connection:
            result = await connection.fetch("SELECT * FROM table1;")
        filtered_result = [record for record in result if record['names'] is not None]
        for record in filtered_result:
            print(record['names'])  

    asyncio.run(main())
