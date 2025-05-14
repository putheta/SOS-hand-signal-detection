# main.py

from handdetection.version4 import detect_hand_sos
from facedetection.v3_testing import process_face_image
path ,location, time = detect_hand_sos()
# if path :  
#     print(f"path : {path}")
#     print(f"location : {location}")
#     print(f"time : {time}")
name = process_face_image(path)
# print(f"Name : {name}")

time = str(time)
date = time[0:10]
time = time[11:19]

Data = {
    "name" : name ,
    "date" : date,
    "time" : time, 
    "location" : location ,
    "picture" : path
}

print(f"Data : {Data}")
