import json
import serial
import sys
import time

port = serial.Serial('COM5')

while True:
    data = json.load(open(sys.argv[1]))
    #port.write(str(data['IlluminateCompLight'].encode()))
    port.write(str(1 if data['IlluminateCompLight'] else 0).encode())
    time.sleep(3)
