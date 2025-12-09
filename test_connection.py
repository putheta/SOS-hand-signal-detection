from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

MONGO_URI = "mongodb+srv://putheta_db_user:1ol0V9e7EaccVWI6@sos-cluster.rgwbko8.mongodb.net/?appName=SOS-Cluster"
async def test_connection():
    try:
        
        AsyncIOMotorClient(MONGO_URI, tls=True)
        client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client["sos-app"]
        collection = db["sos"]

        doc = {"message": "🚨 Hello from another client (local)"}
        result = await collection.insert_one(doc)
        print("✅ Inserted ID:", result.inserted_id)

    except Exception as e:
        print("❌ Error connecting to MongoDB:")
        print(e)

asyncio.run(test_connection())
