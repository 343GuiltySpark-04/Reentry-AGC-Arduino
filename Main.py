import json
import serial
import sys
import time
import os

path_export_apollo = os.path.join(os.environ['APPDATA'], r'..\LocalLow\Wilhelmsen Studios\ReEntry\Export\Apollo')
path_agc_json = os.path.join(path_export_apollo, 'outputAGC.json')
port = serial.Serial('COM5')

while True:
    try:
        data = json.load(open(path_agc_json))
        port.write("#".encode())
        port.write(str(1 if data['IlluminateCompLight'] else 0).encode())
        port.write("V".encode())
        port.write(str(data['VerbD1']).encode())
        port.write(str(data['VerbD2']).encode())
        port.write(" ".encode())
        port.write("N".encode())
        port.write(str(data['NounD1']).encode())
        port.write(str(data['NounD2']).encode())
        port.write(" ".encode())
        port.write("P".encode())
        port.write(str(data['ProgramD1']).encode())
        port.write(str(data['ProgramD2']).encode())
        time.sleep(0.2)
    except json.JSONDecodeError:
        pass
