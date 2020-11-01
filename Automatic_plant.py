import time
import RPi.GPIO as GPIO
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

def reading():
    # Soil Moisture Sensor Readings
    i2c_bus = busio.I2C(SCL, SDA)
    ss = Seesaw(i2c_bus, addr=0x36)
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()
    return touch

moisture= [[]]      # moisture readings every day
day = []            # list of moisture readings every day

for x in range(10):
    for y in range(2):
        day[0] = reading()
        time.sleep(43200)  # 12 hour wait between measurements
        day[1] = reading()
        time.sleep(43200)  # 12 hour wait between measurements
    moisture[x] = day

