  const ws = new WebSocket("ws://localhost:3000");

  ws.onopen = () => {
    console.log("WebSocket connected");
    document.getElementById("logo").src = "static/Group-12.svg";

      if (!sessionStorage.getItem("wsReloaded")) {
        sessionStorage.setItem("wsReloaded", "true");
        location.reload();
      }

  };
  ws.onclose = () => {
    console.warn("WebSocket disconnected");

    if (!sessionStorage.getItem("wsDisconnectedReloaded")) {
      sessionStorage.setItem("wsDisconnectedReloaded", "true");
      location.reload();
    }
  };


  ws.onerror = (err) => {
    console.error("WebSocket error:", err);
 };
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);

    alert("ตรวจพบสัญญาณขอความช่วยเหลือใกล้คุณ!");

    const log = document.getElementById("log");
    log.querySelectorAll("p").forEach(p => p.remove());

    log.innerHTML += `<div class="log-container" onclick="goDetail('${data._id}')">
            <h5>⚠️ มีผู้ส่งสัญญาณขอความช่วยเหลือใกล้คุณ</h5> 
            <hr>
            <p>time : ${JSON.stringify(data.time)}</p>
            <div class="row-container">
                <p>date : ${JSON.stringify(data.date)}</p>
                <button>ดูรายละเอียด</button>
            </div>
          </div>`;

    if (data) {
      console.log("Received data:", data);
      localStorage.setItem("id", data._id);
    }
};

function goDetail(id) {
  window.location.href = `template/detail.html?id=${id}`;
}

