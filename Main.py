import json
import serial
import sys
import time

port = serial.Serial('COM5')

while True:
    data = json.load(open(sys.argv[1]))
    port.write(str(data['IlluminateCompLight'].encode()))
    time.sleep(10)
