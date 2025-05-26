import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(r'C:\Users\puthe\Documents\GitHub\SOS-hand-signal-detection\ML_test\WIN_20250523_12_40_14_Pro.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_threshold = cv2.inRange(frame_HSV, (0,54,88), (174, 255, 255))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    opening = cv2.morphologyEx(frame_threshold, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))
    
    dialation = cv2.dilate(closing,kernel,iterations = 1)
    
    final = cv2.bitwise_and(frame,frame, mask=dialation)
    final_gray = cv2.cvtColor(final,cv2.COLOR_BGR2GRAY)

    contours , _ = cv2.findContours(dialation, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    filtered_mask = np.zeros_like(dialation)
    
    for cnt in contours :
        area = cv2.contourArea(cnt)
        if 20000 < area < 50000 :
            cv2.drawContours(filtered_mask,[cnt],-1,255,-1)
    
    final = cv2.bitwise_and(frame, frame, mask=filtered_mask)
    # คำนวณจุดกลางของเฟรม
    height, width = frame.shape[:2]
    center_x, center_y = width // 2, height // 2

    # วาดจุดตรงกลางเฟรมบนภาพ final
    cv2.circle(frame, (center_x, center_y), 7, (255), -1)  # วาดจุดสีขาว (gray = 255)
    cv2.putText(frame, "Center", (center_x - 40, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255), 1)
    
    cv2.imshow("frame", frame)
    cv2.imshow("cropped", frame_threshold)
    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)


    cv2.imshow("final",final_gray)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
