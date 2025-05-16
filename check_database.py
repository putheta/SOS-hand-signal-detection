from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

MONGO_URI = "mongodb+srv://Punyisa:Mail2004@sos-app.gqbtj58.mongodb.net/?retryWrites=true&w=majority&tls=true&appName=sos-app"

async def fetch_all_docs():
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        db = client["sos-app"]
        collection = db["sos"]

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
