# AGC JSON - Serial Interface client for the AGC Arduino Interface project for Reentry: An Orbital Simulator.
# GitHub Repo: https://github.com/343GuiltySpark-04/Reentry-AGC-Arduino
# And don't forget to grab the Arduino side software from its repo.
# https://github.com/343GuiltySpark-04/AGC_interface_Reentry
# Version: 0.5b
import asyncio
import json
import serial
import sys
import time
import os
import threading
import aiofile

path_export_apollo = os.path.join(os.environ['APPDATA'], r'..\LocalLow\Wilhelmsen Studios\ReEntry\Export\Apollo')
path_agc_json = os.path.join(path_export_apollo, 'outputAGC.json')
port = serial.Serial('COM5')
reg_sel = 0
file_data = {}


async def file_load():
    global file_data
    while True:
        async with aiofile.async_open(path_agc_json, 'r') as f:
            file_data = json.loads(await f.read())

        await asyncio.sleep(0.1)


async def reg_switcher():
    global reg_sel
    while True:
        if reg_sel > 2:
            reg_sel = 0
        reg_sel += 1
        await asyncio.sleep(10)


async def main():
    while True:
        try:
            # data = json.load(open(path_agc_json))

            port.write("#".encode())

            print("#")
            # port.write(str(reg_sel).encode())
            print(reg_sel)
            port.write(str(1 if file_data['IlluminateCompLight'] else 0).encode())
            print(str(file_data['IlluminateCompLight']))
            port.write(str(file_data['IlluminateUplinkActy']).encode())
            port.write("<".encode())
            port.write(str(file_data['Register1Sign']).encode())
            port.write(str(file_data['Register1D1']).encode())
            port.write(str(file_data['Register1D2']).encode())
            port.write(str(file_data['Register1D3']).encode())
            port.write(str(file_data['Register1D4']).encode())
            port.write(str(file_data['Register1D5']).encode())
            port.write(">".encode())
            port.write("$".encode())
            port.write(str(file_data['Register2Sign']).encode())
            port.write(str(file_data['Register2D1']).encode())
            port.write(str(file_data['Register2D2']).encode())
            port.write(str(file_data['Register2D3']).encode())
            port.write(str(file_data['Register2D4']).encode())
            port.write(str(file_data['Register2D5']).encode())
            port.write("%".encode())
            port.write("^".encode())
            port.write(str(file_data['Register3Sign']).encode())
            port.write(str(file_data['Register3D1']).encode())
            port.write(str(file_data['Register3D2']).encode())
            port.write(str(file_data['Register3D3']).encode())
            port.write(str(file_data['Register3D4']).encode())
            port.write(str(file_data['Register3D5']).encode())
            port.write("&".encode())
            port.write("V".encode())
            port.write(str(file_data['VerbD1']).encode())
            port.write(str(file_data['VerbD2']).encode())
            port.write(" ".encode())
            port.write("N".encode())
            port.write(str(file_data['NounD1']).encode())
            port.write(str(file_data['NounD2']).encode())
            port.write(" ".encode())
            port.write("P".encode())
            port.write(str(file_data['ProgramD1']).encode())
            port.write(str(file_data['ProgramD2']).encode())
            time.sleep(0.3)
            # TODO: Spend an hour or so tinkering with the sleep delay!
        except json.JSONDecodeError:
            pass
