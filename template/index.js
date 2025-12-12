  const ws = new WebSocket("ws://localhost:3000");

  ws.onopen = () => {
    console.log("WebSocket connected");
  };

  ws.onerror = (err) => {
    console.error("WebSocket error:", err);
 };
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);

    alert("พบการเพิ่ม Node ใหม่ใน Database!");

    const div = document.getElementById("log");
    div.innerHTML += `<p><b>New Node:</b> ${JSON.stringify(data)}</p>`;
};