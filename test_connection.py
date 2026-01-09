from bson import Binary
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

MONGO_URI = ""
async def test_connection():
    try:
        
        AsyncIOMotorClient(MONGO_URI, tls=True)
        client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client["sos-app"]
        collection = db["sos_alerts"]

       
        doc = {
            "name": "test",
            "date": "2025-12-12",
            "time": "17:33:16",
            "location": [
                13.683342,
                100.610386
            ],
            "image_data": ""
        }
        result = await collection.insert_one(doc)
        print("✅ Inserted ID:", result.inserted_id)

    except Exception as e:
        print("❌ Error connecting to MongoDB:")
        print(e)

asyncio.run(test_connection())
