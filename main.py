# main.py
import os
import cv2
from handdetection.version5 import detect_hand_sos
from facedetection.v4_testing import process_face_image
path ,location, time = detect_hand_sos()
# if path :  
#     print(f"path : {path}")
#     print(f"location : {location}")
#     print(f"time : {time}")
print("path :: ",process_face_image(path))
# print(f"Name : {name}")

time = str(time)
date = time[0:10]
time = time[11:19]

Data = {
    "date" : date,
    "time" : time, 
    "location" : location ,
    "picture" : path
}

