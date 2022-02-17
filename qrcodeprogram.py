from pyzbar.pyzbar import decode
import cv2
import numpy as np
import datetime


#set camera
videoCamera = cv2.VideoCapture(0)
videoCamera.set(3,1280) #width
videoCamera.set(4,1024) #height


while True:
    success,frame = videoCamera.read()
    code= decode(frame)
    for qrcode in decode(frame):
        myData = qrcode.data.decode('utf-8') #output is converted into a string
        print(myData)
        #additional effects
        pts = np.array([qrcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(frame,[pts],True,(0,255,0),3) # set frame width and color
        pts2 = qrcode.rect
        cv2.putText(frame,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.7,(128,128,0),2) # set font, text color
        #convert infos to text file
        textFile = open("data.txt", "w")
        textFile.write(f"{qrcode.data.decode('utf-8')}")
        #set date and time 
        Date = datetime.datetime.now()
        textFile.write(Date.strftime("Date: %m/%d/%y \n"))
        textFile.write(Date.strftime("Time: %H:%M:%S"))  
        textFile.close()
        

    cv2.imshow("Cathleah's QR Scanner", frame)
    #press q to exit camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
