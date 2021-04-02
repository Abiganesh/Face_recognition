# Face_recognition
This repository has face recognition code for Both Images and videos. 

INSTALL LIBRARIES BEFORE USING CODE:
pip install face_recognition
pip install opencv-python

FOR IMAGE:
KEEP ONE KNOWNIMAGE AS ROOT DIR AND INSIDE THE ROOT DIR YOU CAN CREATE N NO.OF.DIR FOR N NO.OF INDIVIDUALS AND ALWAYS NAME THE FOLDER AS THE PERSON'S NAME
KEEP ONE UNKNOWNIMAGE AS ROOT DIR AND KEEP EVERY IMAGES YOU WANT TO CHECK AND YOU SHOULD NOT CREATE ANY DIR OVER THERE
DO NOT NAME YOUR PYTHON AS YOUR LIBRARIES NAMES.

FOR VIDEO:
For Unknown face input Either your you can give your pre recorded video by defining location and filename in cv2.VideoCapture("xyz.mp4) OR you can use your webcam  input by cv2.VideoCapture(0).
