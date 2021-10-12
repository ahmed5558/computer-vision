import cv2
import numpy as np
import serial
import time


circle = 'circle'
triangle = 'triangle'
rectangle = 'rectangle'
goldenLower = (10, 100, 20)
goldenUpper = (25, 255, 255)
blueLower = (110, 50, 0)
blueUpper = (141, 255, 255)
whiteLower = (0, 0, 232)
whiteUpper = (114, 29,255)
brownLower = (51, 0, 0)
brownUpper = (121, 0, 0)
yellowLower = (11, 75, 15)
yellowUpper = (50, 255, 255)
redLower = (0, 152, 0)
redUpper = (255, 196, 254)
orangeLower = (0, 122, 0)
orangeUpper = (28, 192, 255)
greenLower = (27, 187, 0)
greenUpper = (100, 255, 153)
collor = input("collor: ")
shape = input("shape: ")
if 'circle' in shape :
    sh = circle
   
if 'triangle' in shape :
    sh = triangle

if 'rectangle' in shape :
    sh = rectangle
    
if 'red' in collor :
    a = redLower
    b = redUpper
   
if 'yellow' in collor :
    a = yellowLower
    b = yellowUpper

if 'golden' in collor :
    a = yellowLower
    b = yellowUpper
   
if 'blue' in collor :
    a = blueLower
    b = blueUpper    

if 'white' in collor :
    a = whiteLower
    b = whiteUpper
   
if 'green' in collor :
    a = greenLower
    b = greenUpper

if 'orange' in collor :
    a = orangeLower
    b = orangeUpper


def nothing(x):
    # any operation
    pass

#Serial object for communication with Arduino
ser = serial.Serial('com12', 9600, timeout=.1)
#('/dev/ttyACM0')
time.sleep(1)
cap = cv2.VideoCapture(0)

ret = cap.set(3,640)
ret = cap.set(4,480)

font = cv2.FONT_HERSHEY_COMPLEX

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    
    mask = cv2.inRange(hsv, a, b)
    
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)

    # Contours detection
    if int(cv2.__version__[0]) > 3:
        # Opencv 4.x.x
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    else:
        # Opencv 3.x.x
        _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if len(approx) == 3 and sh == triangle and area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            cv2.putText(frame, collor+"Triangle", (x, y), font, 1, (0, 0, 0))
            cv2.line(frame,(320,240), [approx],(0, 0, 255), 1)
            #Reference line
            cv2.line(frame,(320,0),(320,480),(0,255,0),1)

            area = int(area)

            #distance of the 'x' coordinate from the center of the frame
            #wdith of frame is 640, hence 320
            lengths = 320-(int(x))

            #write distance and radius to Arduino through Serial Communication
            ser.write(str('lengths').encode())
            ser.write(str('#').encode())
            ser.write(str('area').encode())
            ser.write(str('/').encode())
        elif len(approx) == 4 and sh == rectangle and area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            cv2.putText(frame, collor+"Rectangle", (x, y), font, 1, (0, 0, 0))
            cv2.line(frame,(320,240), (int(x), int(y)),(0, 0, 255), 1)
            #Reference line
                     
            cv2.line(frame,(320,0),(320,480),(0,255,0),1)

            area = int(area)

            #distance of the 'x' coordinate from the center of the frame
            #wdith of frame is 640, hence 320
            lengths = 320-(int(x))

            #write distance and radius to Arduino through Serial Communication
            ser.write(str('lengths').encode())
            ser.write(str('#').encode())
            ser.write(str('area').encode())
            ser.write(str('/').encode())
        elif 10 < len(approx) < 20 and sh == circle and area > 400:
            
        #Radius and center pixel coordinate of the largest contour
            
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            #cv2.putText(frame, collor+"Circle", (x, y), font, 1, (0, 0, 0))
            cv2.line(frame,(320,240), [approx],(0, 0, 255), 1)
            #Reference line
            cv2.line(frame,(320,0),(320,480),(0,255,0),1)

            area = int(area)

            #distance of the 'x' coordinate from the center of the frame
            #wdith of frame is 640, hence 320
            lengths = 320-(int(x))

            #write distance and radius to Arduino through Serial Communication
            ser.write(str('lengths').encode())
            ser.write(str('#').encode())
            ser.write(str('area').encode())
            ser.write(str('/').encode())
            
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
