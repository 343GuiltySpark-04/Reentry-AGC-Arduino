import json
import serial
import sys
import time
import os

path_export_apollo = os.path.join(os.environ['APPDATA'], r'..\LocalLow\Wilhelmsen Studios\ReEntry\Export\Apollo')
path_agc_json = os.path.join(path_export_apollo, 'outputAGC.json')
port = serial.Serial('COM5')

while True:
    #data = json.load(open(sys.argv[1]))
    data = json.load(open(path_agc_json))
    port.write(str(1 if data['IlluminateCompLight'] else 0).encode())
    time.sleep(3)
