const overlay = document.querySelector(".background");
const popupTitle = document.getElementById("popupTitle");
const popupContent = document.getElementById("popupContent");
const popupImage = document.getElementById("popupImage");

const contents = {
  intro: {
    title: "คำแนะนำการใช้งานแอปพลิเคชัน",
    html: `
      <p class="discription">
        แอปพลิเคชันนี้ใช้สำหรับแจ้งเตือนเมื่อระบบตรวจพบสัญญาณมือขอความช่วยเหลือ (SOS)
        เพื่อให้ผู้ที่อยู่ใกล้เคียงช่วยกันสังเกตและยืนยันสถานการณ์
      </p>
      <ul>
        <li>เมื่อระบบตรวจพบสัญญาณมือ SOS จะมีการแจ้งเตือนมายังแอปของคุณ</li>
        <li>กรุณาสังเกตสถานการณ์และบุคคลในบริเวณใกล้เคียงอย่างรอบคอบ</li>
        <li>หากพบสถานการณ์ที่มีความเสี่ยง
            ให้กดปุ่ม รายงาน เพื่อร่วมยืนยันสัญญาณ</li>
        <li>ระบบจะส่งข้อมูลไปยังเจ้าหน้าที่ที่เกี่ยวข้อง</li>
      </ul>
    `
  },

info: {
  title: "ข้อมูลเกี่ยวกับสัญญาณมือขอความช่วยเหลือ (SOS)",
  html: `
    <p class="discription">
      สัญญาณมือขอความช่วยเหลือ (Signal for Help) คือสัญญาณมือที่ใช้เพื่อบอกผู้อื่นอย่างเงียบ ๆ
      ว่าผู้ส่งสัญญาณกำลังอยู่ในสถานการณ์ไม่ปลอดภัยและต้องการความช่วยเหลือ
      โดยไม่จำเป็นต้องพูดหรือส่งเสียง
    </p>

    <p class="discription">
      สัญญาณนี้ถูกออกแบบมาเพื่อใช้ในสถานการณ์ที่ไม่สามารถขอความช่วยเหลือได้อย่างเปิดเผย
      เช่น ความรุนแรงในครอบครัว หรือสถานการณ์คุกคามอื่น ๆ
      และสามารถใช้ได้ทั้งในชีวิตจริงและการสื่อสารผ่านวิดีโอ
    </p>

    <ul>
      <li>ยกมือขึ้นให้เห็นฝ่ามือ</li>
      <li>พับนิ้วโป้งเข้าหาฝ่ามือ</li>
      <li>กำมือโดยใช้นิ้วที่เหลือปิดทับนิ้วโป้ง</li>
      <li>ทำท่าทางเป็นการเคลื่อนไหวต่อเนื่อง เพื่อให้ผู้อื่นสังเกตเห็น</li>
    </ul>

    <p class="discription">
      หากพบเห็นสัญญาณนี้ ควรตอบสนองอย่างระมัดระวัง
      เช่น การสอบถามด้วยวิธีที่ปลอดภัย และหลีกเลี่ยงการกระทำที่อาจเพิ่มความเสี่ยงให้กับผู้ส่งสัญญาณ
    </p>
  `
}

};

document.querySelectorAll(".banner").forEach(banner => {
  banner.addEventListener("click", () => {
    const type = banner.dataset.type;
    const data = contents[type];

    popupTitle.innerText = data.title;
    popupContent.innerHTML = data.html;
    popupImage.src = banner.src;

    overlay.classList.remove("hide");
  });
});

document.getElementById("close-button").addEventListener("click", () => {
  overlay.classList.add("hide");
});
