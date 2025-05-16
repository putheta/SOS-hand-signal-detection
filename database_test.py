from motor.motor_asyncio import AsyncIOMotorClient
import asyncio


async def test_connection():
    client = AsyncIOMotorClient("mongodb://172.21.237.228:27017")
    db = client["sos_database"]
    collection = db["sos_alerts"]

    doc = {"message": "🚨 Hello from another client (local)"}
    result = await collection.insert_one(doc)
    print("✅ Inserted ID:", result.inserted_id)

asyncio.run(test_connection())
