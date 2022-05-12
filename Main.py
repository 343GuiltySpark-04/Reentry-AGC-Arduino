import serial, sys, json, time

port = serial.Serial('COM5')

while True:
    data = json.load(open(sys.argv[1]))
    port.write(str(data['IlluminateUplinkActy'].encode()))
    time.sleep(10)