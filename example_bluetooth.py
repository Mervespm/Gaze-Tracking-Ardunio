"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import serial
import time


gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

#port="COM4"
port="/dev/tty.HC-06"
#seriport = serial.Serial(port = "/dev/tty.HC-06", baudrate= 9600, timeout= 0.1) # serial
bluetooth=serial.Serial(port, 9600)


oldTime = 0

while True:
    bluetooth.flushInput()
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    
    newTime = time.perf_counter()
    dif = newTime - oldTime
    
    if dif > 5:
    	oldTime = newTime
    
    	text = ""
    	value = 3

        #serialString = seriport.readline()
        # time.sleep(0.05)
        #dencoded_byte = serialString.decode('utf-8')
        # print(dencoded_byte)
        #data = dencoded_byte.split("*") 


        if len(data) <= 4:
            continue
        else:

        	if gaze.is_right(): #Right:1
        		value = 1
        		text = "Looking right: " + str(value)
        		bluetooth.write(b"R")
                #seriport.write('2'.encode())
        	elif gaze.is_left(): #Left:-1
            	value = -1
            	text = "Looking left: " + str(value)
            	bluetooth.write(b"L")
                #seriport.write('1'.encode())
        	elif gaze.is_looking_up(): #Up:2
            	value = 2
            	text = "Looking up: " + str(value)
            	bluetooth.write(b"F")
                #seriport.write('3'.encode())
        	elif gaze.is_looking_down(): #Down:-2
            	value = -2
            	text = "Looking down: " + str(value)
            	bluetooth.write(b"B")
                #seriport.write('4'.encode())
        	elif gaze.is_center(): #Center:0
            	value = 0
            	text = "Looking center: " + str(value)
                #seriport.write('5'.encode())
            	bluetooth.write(b"O")

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
bluetooth.close()  
webcam.release()
cv2.destroyAllWindows()

