import express from "express";
import { WebSocketServer } from "ws";
import { MongoClient } from "mongodb";

const app = express();
const PORT = 3000;

// --- WebSocket Server ---
const wss = new WebSocketServer({ noServer: true });

// --- HTTP server สำหรับอัปเกรดเป็น WebSocket ---
const server = app.listen(PORT, () => {
  console.log("Server running on port", PORT);
});

server.on("upgrade", (req, socket, head) => {
  wss.handleUpgrade(req, socket, head, (ws) => {
    wss.emit("connection", ws, req);
  });
});

// --- MongoDB Atlas ---
const uri = "mongodb+srv://putheta_db_user:1ol0V9e7EaccVWI6@sos-cluster.rgwbko8.mongodb.net/?appName=SOS-ClusterYOUR_MONGODB_ATLAS_CONNECTION_STRING";

const client = new MongoClient(uri);

async function run() {
  await client.connect();
  const db = client.db("testdb");
  const collection = db.collection("nodes");

  console.log("Connected to MongoDB Atlas");

  // เปิด Change Stream เฝ้าดูการ insert
  const changeStream = collection.watch([{ $match: { operationType: "insert" } }]);

  changeStream.on("change", (change) => {
    console.log("New node inserted:", change.fullDocument);

    // ส่งข้อมูลไปยังทุก WebSocket client
    wss.clients.forEach((client) => {
      client.send(JSON.stringify(change.fullDocument));
    });
  });
}

run();
