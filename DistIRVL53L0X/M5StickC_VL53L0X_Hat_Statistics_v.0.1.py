"""
MicroPython for M5StickC - VL53L0X Hat
Version: 0.1
Author: Thiago Ferreira Santos
E-mail: thiago_fisica@outlook.com
Date: 25-26/03/2020
Performs 50 readings and displays the mean, variance and standard deviation
Example from M5Stack: https://github.com/m5stack/UIFlow-Code/wiki/Unit#tof
"""


from m5stack import lcd
from m5ui import M5TextBox, M5Title, setScreenColor
from uiflow import wait_ms
import time
import hat
import math

lcd.clear()
lcd.setRotation(3)
distfield = M5TextBox(40, 20, "0", lcd.FONT_DejaVu40, 0x08feab)
distlabel = M5TextBox(0, 0, "M5Stick VL53L0X Hat", lcd.FONT_Small, 0xFFFFFF)

tof = hat.get(hat.TOF)

def mean(readings):
    sumHat = 0
    for x in readings:
        sumHat += x

    return sumHat/len(readings)

def variance(readings):
    meanHat = mean(readings)
    variance = 0

    for x in readings:
        variance += (x - meanHat)**2

    variance = variance/(len(readings) - 1)
    return variance

def stdev(readings):
    return math.sqrt(variance(readings))

numReadings = []

while True:
    for i in range(50):
        distfield.setText(str(tof.GetDistance()))
        delta_tof = 1 + (tof.GetDistance()*3//100)
        numReadings.append(tof.GetDistance)
        wait_ms(60)

    print("MicroPython v1.11-321; ESP32 module with ESP32 - M5StickC VL53L0X Hat: Statistics distance")
    print("Mean = {:.3f} mm, Variance = {:.3f}, Standard deviation = {:.3f} \n \n".format(mean(numReadings), variance(numReadings), stdev(numReadings)))
    numReadings = []
