from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import traceback
from handdetection.version5 import detect_hand_sos
from facedetection.v4_testing import process_face_image

from bson.binary import Binary

MONGO_URI = "mongodb+srv://putheta_db_user:1ol0V9e7EaccVWI6@sos-cluster.rgwbko8.mongodb.net/?appName=SOS-Cluster"

async def test_sending():
    try:
        # เรียกฟังก์ชันประมวลผลภาพ
        abs_path, location, full_time = detect_hand_sos()
        name = process_face_image(abs_path)

        # แยกวันที่ เวลา
        full_time = str(full_time)
        date = full_time[:10]
        time = full_time[11:19]

        # สร้าง path แบบ URL
        split_index = abs_path.lower().find("static")
        if split_index == -1:
            raise ValueError("Static path not found in image path.")
        url_path = "/" + abs_path[split_index:].replace("\\", "/")
        
        with open(abs_path,"rb") as f :
            image_data = f.read()

        data = {
            "name": "person",
            "date": date,
            "time": time,
            #"location": location
            "location": [13.683342, 100.610386]
            ,"image_data" : Binary(image_data)
            #, "path": url_path
        }

        client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client["sos-app"]
        collection = db["sos_alerts"]

        result = await collection.insert_one(data)
        print("✅ Inserted ID:", result.inserted_id)

    except Exception as e:
        print("❌ Error sending data to  MongoDB:")
        traceback.print_exc()

asyncio.run(test_sending())
