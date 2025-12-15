// ====== WebSocket URL แบบ dynamic ======
const protocol = location.protocol === "https:" ? "wss" : "ws";
const ws = new WebSocket(`${protocol}://${location.host}`);

let hasReloadedOnConnect = false;

ws.onopen = () => {
  console.log("WebSocket connected");

  document.getElementById("logo").src = "/static/Group-12.svg";

  // ✅ reload แค่ครั้งเดียว (กรณีเปิดหน้ามาก่อน server พร้อม)
  if (!hasReloadedOnConnect && !sessionStorage.getItem("ws_connected")) {
    sessionStorage.setItem("ws_connected", "true");
    hasReloadedOnConnect = true;
    location.reload();
  }
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);

  console.log("Received data:", data);

  alert("⚠️ ตรวจพบสัญญาณขอความช่วยเหลือใกล้คุณ!");

  const log = document.getElementById("log");
  log.innerHTML = ""; // ล้างข้อความเก่า

  log.innerHTML = `
    <div class="log-container" onclick="goDetail('${data._id}')">
      <h5>⚠️ มีผู้ส่งสัญญาณขอความช่วยเหลือใกล้คุณ</h5>
      <hr>
      <p>time : ${data.time}</p>
      <div class="row-container">
        <p>date : ${data.date}</p>
        <button>ดูรายละเอียด</button>
      </div>
    </div>
  `;

  // เก็บ id ไว้ เผื่อ refresh
  localStorage.setItem("lastSOSId", data._id);
};

ws.onerror = (err) => {
  console.error("WebSocket error:", err);
};

ws.onclose = () => {
  console.warn("WebSocket disconnected");

  // ✅ reload แบบหน่วง (กัน reload รัว)
  if (!sessionStorage.getItem("ws_disconnected")) {
    sessionStorage.setItem("ws_disconnected", "true");

    setTimeout(() => {
      location.reload();
    }, 2000); // รอ 2 วิ
  }
};

// ====== navigation ======
function goDetail(id) {
  window.location.href = `/detail?id=${id}`;
}
