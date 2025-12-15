import express from "express";
import { WebSocketServer } from "ws";
import { MongoClient, ObjectId } from "mongodb";
import cors from "cors";
import path from "path";
import { fileURLToPath } from "url";

// ====== FIX __dirname (ES module) ======
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// ====== สร้าง app ก่อน (สำคัญมาก) ======
const app = express();
const PORT = 3000;

app.use(cors());

// ====== serve static files ======
app.use(express.static(path.join(__dirname, "public")));

// ====== MongoDB ======
const uri =
  "mongodb+srv://putheta_db_user:1ol0V9e7EaccVWI6@sos-cluster.rgwbko8.mongodb.net/?appName=SOS-Cluster";

const client = new MongoClient(uri);
let collection;

async function startServer() {
  await client.connect();
  console.log("Connected to MongoDB Atlas");

  const db = client.db("sos-app");
  collection = db.collection("sos_alerts");

  // ====== WebSocket ======
  const wss = new WebSocketServer({ noServer: true });

  const server = app.listen(PORT, () => {
    console.log("Server running on port", PORT);
  });

  server.on("upgrade", (req, socket, head) => {
    wss.handleUpgrade(req, socket, head, (ws) => {
      wss.emit("connection", ws, req);
    });
  });

  const changeStream = collection.watch([
    { $match: { operationType: "insert" } },
  ]);

  changeStream.on("change", (change) => {
    console.log("New node inserted:", change.fullDocument);
    wss.clients.forEach((client) => {
      client.send(JSON.stringify(change.fullDocument));
    });
  });

  // ====== API ======
  app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "template", "index.html"));
  });

  app.get("/detail", (req, res) => {
    res.sendFile(path.join(__dirname, "template", "detail.html"));
  });

  app.get("/sos/:id", async (req, res) => {
    try {
      const { id } = req.params;

      if (!ObjectId.isValid(id)) {
        return res.status(400).json({ message: "Invalid ID format" });
      }

      const data = await collection.findOne({
        _id: new ObjectId(id),
      });

      if (!data) {
        return res.status(404).json({ message: "Data not found" });
      }

      res.json(data);
    } catch (error) {
      console.error("Error Fetching data:", error);
      res.status(500).json({ message: "Internal Server Error" });
    }
  });
}

startServer();
