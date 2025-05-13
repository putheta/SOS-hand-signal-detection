import cv2
import face_recognition
import mediapipe as mp
import os
import numpy as np

os.chdir(os.path.dirname(__file__))


# Load known faces and encode them
known_encodings = []
known_names = []



# ตรวจสอบไฟล์ในโฟลเดอร์ known_faces
if not os.path.exists("known_faces"):
    print("⚠️ ไม่พบโฟลเดอร์ 'known_faces'")
else:
    for filename in os.listdir("known_faces"):
        if filename.endswith(".jpg"):
            print(f"กำลังโหลด: {filename}")
            image = face_recognition.load_image_file(f"known_faces/{filename}")
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])

# Set up MediaPipe face detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as detector:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ ไม่สามารถอ่านจากกล้องได้")
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = detector.process(rgb)

        if result.detections:
            for det in result.detections:
                bbox = det.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x1 = int(bbox.xmin * w)
                y1 = int(bbox.ymin * h)
                x2 = int((bbox.xmin + bbox.width) * w)
                y2 = int((bbox.ymin + bbox.height) * h)

                # Crop the face for recognition
                face_crop = rgb[y1:y2, x1:x2]
                face_encoding = face_recognition.face_encodings(face_crop)

                if face_encoding:
                    print("✅ เจอใบหน้าและมีการแปลงเป็น encoding แล้ว")
                    # Compare the face with known faces
                    matches = face_recognition.compare_faces(known_encodings, face_encoding[0])
                    name = "Unknown"
                    
                    # Find the best match (lowest distance)
                    face_distances = face_recognition.face_distance(known_encodings, face_encoding[0])
                    best_match_index = np.argmin(face_distances)
                    
                    if matches[best_match_index]:
                        name = known_names[best_match_index]

                    # Draw bounding box and name
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                else:
                    print("❌ ไม่พบ encoding ของใบหน้า")
        else:
            print("😕 ไม่เจอใบหน้า")

        # Show the frame
        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
