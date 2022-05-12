import serial, sys, json, time

ser = serial.Serial('COM3')

while True:
    j = json.load(open(sys.argv[1]))
    ser.write(str(j['IlluminateUplinkActy'].encode()))
    time.sleep(10)