from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

MONGO_URI = "mongodb+srv://Punyisa:Mail2004@sos-app.gqbtj58.mongodb.net/?retryWrites=true&w=majority&appName=sos-app"
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
