import numpy as np
import cv2 
from tensorflow.keras.models import load_model

model = load_model(r"C:\Users\puthe\Documents\GitHub\SOS-hand-signal-detection\ML_test\hand_gesture_model.keras")

class_names = ["0","4","5"]

cap = cv2.VideoCapture(0)
while True :
    ret, frame = cap.read()
    
    roi = frame[100:324 ,100:324]
    
    img = cv2.resize(roi, (224, 224))
    img = img / 255.0  # normalize
    img = np.expand_dims(img, axis=0)
    
    pred = model.predict(img)
    pred_class = class_names[np.argmax(pred)]
    
    cv2.rectangle(frame, (100, 100), (324, 324), (0, 255, 0), 2)
    cv2.putText(frame, f'Gesture: {pred_class}', (100, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Hand Gesture Detection', frame)
    
    img = np.expand_dims(img, axis=0)  
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
