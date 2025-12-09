from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

MONGO_URI = "mongodb+srv://putheta_db_user:1ol0V9e7EaccVWI6@sos-cluster.rgwbko8.mongodb.net/?appName=SOS-Cluster"

async def fetch_all_docs():
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        db = client["sos-app"]
        collection = db["sos_alerts"]

        # cursor = collection.find({})  # หาเอกสารทั้งหมด
        cursor = collection.find({}, {"image_data": 0})  # Excludes image_data from results
        documents = await cursor.to_list(length=None)

        print("📄 ทั้งหมด:", len(documents))
        for i, doc in enumerate(documents, 1):
            print(f"\n🔢 Document {i}:")
            print(doc)

    except Exception as e:
        print("❌ Error fetching documents:", e)

asyncio.run(fetch_all_docs())
