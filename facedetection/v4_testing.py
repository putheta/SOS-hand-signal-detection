import os
import cv2
import mediapipe as mp
import numpy as np

def process_face_image(image_path: str):
    # ตรวจสอบว่าไฟล์ภาพมีอยู่จริง
    if not os.path.exists(image_path):
        print(f"❌ ไม่พบไฟล์ภาพ: {image_path}")
        return

    # โหลดภาพและแปลงเป็น RGB
    frame = cv2.imread(image_path)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # ใช้ MediaPipe ตรวจจับใบหน้า
    mp_face_detection = mp.solutions.face_detection
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as detector:
        result = detector.process(rgb)

        if result.detections:
            for det in result.detections:
                bbox = det.location_data.relative_bounding_box
                h, w, _ = frame.shape

                x1 = int(bbox.xmin * w)
                y1 = int(bbox.ymin * h)
                x2 = int((bbox.xmin + bbox.width) * w)
                y2 = int((bbox.ymin + bbox.height) * h)

                # ป้องกัน crop index หลุด
                x1 = max(0, x1)
                y1 = max(0, y1)
                x2 = min(w, x2)
                y2 = min(h, y2)

                # ครอปใบหน้า
                face_crop = rgb[y1:y2, x1:x2]
                face_region = frame[y1:y2, x1:x2]
                # ตรวจว่าครอปมีข้อมูลจริงไหม
                if face_crop.size > 0:
                    # วาดกรอบบนรูปต้นฉบับ
                    blurred_face = cv2.GaussianBlur(face_region, (77, 77), 30)
                    frame[y1:y2, x1:x2] = blurred_face
                    cv2.imwrite(image_path, frame)
                else:
                    print("❌ ครอปใบหน้าไม่ได้ (crop ว่าง)")

        else:
            print("😕 ไม่เจอใบหน้าในภาพ")

    # แสดงผลลัพธ์
    cv2.imshow("Result", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return None