const params = new URLSearchParams(window.location.search);
const id = params.get("id");

console.log("Detail page ID:", id);

fetch(`http://localhost:3000/sos/${id}`)
  .then(res => res.json())
  .then(data => {
    console.log("MongoDB data:", data);

    const lat = data.location[0];
    const lng = data.location[1];

    // สร้างแผนที่
    const map = L.map("map").setView([lat, lng], 15);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "© OpenStreetMap"
    }).addTo(map);

    // จุดตำแหน่ง
    L.marker([lat, lng]).addTo(map);

    // วงรัศมี 150m
    L.circle([lat, lng], {
      radius: 150,
      color: "red",
      fillColor: "#ff4d4d",
      fillOpacity: 0.2,
    }).addTo(map);

    // รายละเอียด
    document.getElementById("time").innerText =
      `${data.time}`;
    document.getElementById("date").innerText =
      `${data.date}`;

    document.getElementById("distance").innerText = "150";
  })
  .catch(err => console.error(err));

const toggle = document.getElementById("toggleDetail");
const content = document.getElementById("detailContent");
const chevron = document.getElementById("chevron");

toggle.addEventListener("click", () => {
  content.classList.toggle("hidden");
  chevron.classList.toggle("rotate");
});
