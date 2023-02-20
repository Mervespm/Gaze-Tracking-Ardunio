"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import serial
import time
import socket

serial_speed = 9600
serial_port = '/dev/tty.HC-06'

ADDR = '98D371F9991'
PORT = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((ADDR, PORT))

#ser = serial.Serial(serial_port, serial_speed, timeout=1)
#ser.flushInput()
while True:
    s.send(bytes(0x55))
    time.sleep(0.01)
    
#ser.close()  


