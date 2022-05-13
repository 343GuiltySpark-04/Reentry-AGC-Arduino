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
        port.write(str(data['IlluminateStby']).encode())
        port.write(str(data['IlluminateUplinkActy']).encode())
        port.write(str(data['IlluminateOprErr']).encode())
        port.write(str(data['IlluminateKeyRel']).encode())
        port.write(str(data['IlluminateNoAtt']).encode())
        port.write(str(data['IlluminateTemp']).encode())
        port.write(str(data['IlluminateGimbalLock']).encode())
        port.write(str(data['IlluminateProg']).encode())
        port.write(str(data['IlluminateRestart']).encode())
        port.write(str(data['IlluminateTracker']).encode())
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
