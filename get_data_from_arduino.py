import time
import serial
from vpython import *
from voltmeter import visualize_data

voltage_data = serial.Serial("com3", 115200)  # com1 is a com port of your arduino
time.sleep(1)
oldPot = 0
scaling_factor = 1.0
needle, needleRange = visualize_data()

while True:
    while voltage_data.inWaiting() == 0:
        pass
    data_stor = voltage_data.readline()
    data_stor = str(data_stor, "utw-8")
    clean_data = int(data_stor.strip("\r\n"))
    voltage = round(((3.3 / 1023.0) * clean_data), 2)

    deltaPot = oldPot - int(voltage)
    deltaNeedleAngle = needleRange * (deltaPot / 1023) * scaling_factor
    needle.rotate(deltaNeedleAngle, axis=vector(0, 0, 1), origin=vector(0, -0.4, 0.08))
    oldPot = int(voltage)
    rate(10)
