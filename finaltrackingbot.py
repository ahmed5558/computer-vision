import cv2
import numpy as np
import serial
import time


red = 'red'
green = 'green'
blue = 'blue'
orange = 'orange'
yellow = 'yellow'
white = 'white'
hexagon = 'hexagon'
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

collor = input("choose collor (1 for red) (2 for green) (3 for blue) (4 for orange) (5 for yellow) (6 for white) then press enter: ")
shape = input("choose shape (11 for rectangle)(12 for triangle)(13 for circle)(14 for hexagon) then press enter: ")
if '13' in shape :
    sh = circle
   
if '12' in shape :
    sh = triangle

if '11' in shape :
    sh = rectangle

if '14' in shape :
    sh = hexagon    
    
if '1' in collor :
    a = redLower
    b = redUpper
    collor = red
   
if '5' in collor :
    a = yellowLower
    b = yellowUpper
    collor = yellow
    
if '3' in collor :
    a = blueLower
    b = blueUpper    
    collor = blue

if '6' in collor :
    a = whiteLower
    b = whiteUpper
    collor = white
   
if '2' in collor :
    a = greenLower
    b = greenUpper
    collor = green

if '4' in collor :
    a = orangeLower
    b = orangeUpper
    collor = orange

def nothing(x):
    # any operation
    pass

#Serial object for communication with Arduino
ser = serial.Serial('com11', 9600)
#('/dev/ttyACM0')
time.sleep(2)
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
        
        if len(approx) == 3 and sh == triangle and area > 200:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            cv2.putText(frame, collor+"Triangle", (x, y), font, 1, (0, 0, 0))
            cv2.line(frame,(320,240), (int(x), int(y)),(0, 0, 255), 1)
            #Reference line
            cv2.line(frame,(320,0),(320,480),(0,255,0),1)

            if x < 300  :
                ser.write(b'3')
                #ser.write(b'2')
            elif x > 340 :
                ser.write(b'4')
                #ser.write(b'2')
            elif x > 300 and x < 340 :
                ser.write(b'2')
            if area >100 and area < 2000 :
                ser.write(b'1')
            elif area > 8000 :
                ser.write(b'0')
            elif area > 2000 and area < 7000 :
                ser.write(b'2')
            print (area)
            
        elif len(approx) == 4 and sh == rectangle and area > 200 :
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            cv2.putText(frame, collor+"Rectangle", (x, y), font, 1, (0, 0, 0))
            cv2.line(frame,(320,240), (int(x), int(y)),(0, 0, 255), 1)
            #Reference line
                     
            cv2.line(frame,(320,0),(320,480),(0,255,0),1)

            if x < 250  :
                ser.write(b'3')
                #ser.write(b'2')
            elif x > 390 :
                ser.write(b'4')
                #ser.write(b'2')
            elif x > 250 and x < 390 :
                ser.write(b'2')
            time.sleep(0)
            if area >100 and area < 2000 :
                ser.write(b'1')
            elif area > 8000 :
                ser.write(b'0')
            elif area > 2000 and area < 7000 :
                ser.write(b'2')
            
            print (area)
        elif 10 < len(approx) < 20 and sh == circle and area > 200:
            
        #Radius and center pixel coordinate of the largest contour
            
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            cv2.putText(frame, collor+"Circle", (x, y), font, 1, (0, 0, 0))
            cv2.line(frame,(320,240), (int(x), int(y)),(0, 0, 255), 1)
            #Reference line
            cv2.line(frame,(320,0),(320,480),(0,255,0),1)

            if x < 300  :
                ser.write(b'3')
                #ser.write(b'2')
            elif x > 340 :
                ser.write(b'4')
                #ser.write(b'2')
            elif x > 300 and x < 340 :
                ser.write(b'2')
            if area >100 and area < 2000 :
                ser.write(b'1')
            elif area > 8000 :
                ser.write(b'0')
            elif area > 2000 and area < 7000 :
                ser.write(b'2')
            print (area)
        elif len(approx) == 6 and sh == hexagon and area > 200:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            cv2.putText(frame, collor+"hexagon", (x, y), font, 1, (0, 0, 0))
            cv2.line(frame,(320,240), (int(x), int(y)),(0, 0, 255), 1)
            #Reference line
            cv2.line(frame,(320,0),(320,480),(0,255,0),1)

            if x < 300  :
                ser.write(b'3')
                #ser.write(b'2')
            elif x > 340 :
                ser.write(b'4')
                #ser.write(b'2')
            elif x > 300 and x < 340 :
                ser.write(b'2')
            if area >100 and area < 2000 :
                ser.write(b'1')
            elif area > 8000 :
                ser.write(b'0')
            elif area > 2000 and area < 7000 :
                ser.write(b'2')
            print (area)
            
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
