import numpy as np
import cv2
import time
import os

IMAGE_PATH = './images'
label = '0'

isExist = os.path.exists(os.path.join(IMAGE_PATH, label))
if isExist:
    directory = os.path.join(IMAGE_PATH, label)
else:
    directory = os.path.join(IMAGE_PATH, label)
    os.mkdir(directory)

# use gstreamer for video directly; set the fps
camSet='v4l2src device=/dev/video0 ! video/x-raw,framerate=30/1 ! videoconvert ! video/x-raw, format=BGR ! appsink'
cap= cv2.VideoCapture(camSet)
#cap = cv2.VideoCapture(0)

i = 0
while(True):
    # Capture frame-by-frame
    print("Taking picture", i,"...")
    time.sleep(2)
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame',frame)
    
    imgname = os.path.join(directory, label+'-'+'{}.jpg'.format(str(i)))
    print('Capturing',imgname)
    cv2.imwrite(imgname, frame)
    #time.sleep(2)

    i += 1
    
    if i in [15, 30, 45]:
        print('Change camera setting!')
        time.sleep(5)
    
    if i == 68:
        print('Finish capturing label', label)
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
