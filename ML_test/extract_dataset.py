import cv2
import os

# --- SETTINGS ---
video_path = r'C:\Users\puthe\Documents\GitHub\SOS-hand-signal-detection\ML_test\WIN_20250523_12_40_14_Pro.mp4'         # Replace with your video file path
gesture_label = '0'                   # Change to '4' or '0' for other gestures
output_dir = 'dataset'                # Root folder to save images
frame_skip = 5                        # Save every 5th frame to reduce redundancy

# --- SETUP OUTPUT PATH ---
gesture_dir = os.path.join(output_dir, gesture_label)
os.makedirs(gesture_dir, exist_ok=True)

# --- LOAD VIDEO ---
cap = cv2.VideoCapture(video_path)
frame_count = 0
saved_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_skip == 0:
        # Resize frame (optional)
        frame = cv2.resize(frame, (224, 224))  # Resize to match input model size

        # Save frame
        filename = f"{gesture_label}_{saved_count:04d}.jpg"
        cv2.imwrite(os.path.join(gesture_dir, filename), frame)
        saved_count += 1

    frame_count += 1

cap.release()
print(f"✅ Saved {saved_count} frames to '{gesture_dir}'")
