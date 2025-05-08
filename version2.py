import cv2
import mediapipe as mp

vid = cv2.VideoCapture(0)
check = [0,0]
mphands = mp.solutions.hands
Hands = mphands.Hands(max_num_hands= 1, min_detection_confidence= 0.7, min_tracking_confidence= 0.6 )
mpdraw = mp.solutions.drawing_utils
font = cv2.FONT_HERSHEY_SIMPLEX
count = 0
top = 0
bottom = 0

while True :
    check = [0,0]
    _, frame = vid.read()
    # convert from bgr to rgb
    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = Hands.process(RGBframe)
    
    if result.multi_hand_landmarks:
        #print("hand found")
        for handLm in result.multi_hand_landmarks :
            #print(handLm)
            mpdraw.draw_landmarks(frame, handLm, mphands.HAND_CONNECTIONS,
                                 mpdraw.DrawingSpec(color=(0, 0, 255), circle_radius=7,
                                                    thickness=cv2.FILLED),
                                 mpdraw.DrawingSpec(color=(0, 255, 0), thickness=5)
                                 )
            for id, lm in enumerate(handLm.landmark):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
            #    print(id, cx, cy)

               # cv2.circle(frame, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
                if id == 12 :
                   Tx_12 , Ty_12 = cx,cy
                   top = Ty_12
                if id == 0 :
                    Tx_0 , Ty_0 = cx,cy
                    bottom = Ty_0
                    frame_ready = True
                    
                   
    h, w, _ = frame.shape         
    print("height" ,h)     
    try :
        if frame_ready and 0 <= top < bottom <= h :
            cropped = frame[top:bottom, 0:w]
            cv2.imshow("Cropped", cropped)
    except:
        # ถ้ายังไม่พร้อม แสดงภาพเต็ม
        cv2.imshow("Cropped", frame)
        
    cv2.imshow("video", frame)

    
    if cv2.waitKey(1) != -1:
        break

vid.release()
cv2.destroyAllWindows()
