# AGC JSON - Serial Interface client for the AGC Arduino Interface project for Reentry: An Orbital Simulator.
# GitHub Repo: https://github.com/343GuiltySpark-04/Reentry-AGC-Arduino
# And don't forget to grab the Arduino side software from its repo.
# https://github.com/343GuiltySpark-04/AGC_interface_Reentry
# Version: 0.4c


import json
import serial
import sys
import time
import os
import threading

path_export_apollo = os.path.join(os.environ['APPDATA'], r'..\LocalLow\Wilhelmsen Studios\ReEntry\Export\Apollo')
path_agc_json = os.path.join(path_export_apollo, 'outputAGC.json')
port = serial.Serial('COM5')
thread_started = False
reg_sel = 1


class Reader(threading.Thread):

    def __init__(self, null):
        threading.Thread.__init__(self)
        self.null = null

    def run(self):

        global reg_sel
        while True:

            if reg_sel > 3:
                reg_sel = 1
            reg_sel += 1
            time.sleep(5)


while True:
    try:
        data = json.load(open(path_agc_json))
        t = Reader('null')
        port.write("#".encode())
        t.start()
        print("#")
        port.write(str(reg_sel).encode())
        print(reg_sel)
        port.write(str(1 if data['IlluminateCompLight'] else 0).encode())
        print(str(data['IlluminateCompLight']))
        port.write(str(data['IlluminateUplinkActy']).encode())
        port.write("<".encode())
        port.write(str(data['Register1Sign']).encode())
        port.write(str(data['Register1D1']).encode())
        port.write(str(data['Register1D2']).encode())
        port.write(str(data['Register1D3']).encode())
        port.write(str(data['Register1D4']).encode())
        port.write(str(data['Register1D5']).encode())
        port.write(">".encode())
        port.write("$".encode())
        port.write(str(data['Register2Sign']).encode())
        port.write(str(data['Register2D1']).encode())
        port.write(str(data['Register2D2']).encode())
        port.write(str(data['Register2D3']).encode())
        port.write(str(data['Register2D4']).encode())
        port.write(str(data['Register2D5']).encode())
        port.write("%".encode())
        port.write("^".encode())
        port.write(str(data['Register3Sign']).encode())
        port.write(str(data['Register3D1']).encode())
        port.write(str(data['Register3D2']).encode())
        port.write(str(data['Register3D3']).encode())
        port.write(str(data['Register3D4']).encode())
        port.write(str(data['Register3D5']).encode())
        port.write("&".encode())
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
        time.sleep(0.3)
        # TODO: Spend an hour or so tinkering with the sleep delay!
    except json.JSONDecodeError:
        pass
