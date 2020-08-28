"""
MicroPython for M5StickC - VL53L0X Unit
Version: 0.1
Author: Thiago Ferreira Santos
E-mail: thiago_fisica@outlook.com
Date: 17-20/03/2020
Performs 60 readings and displays the mean, standard deviation and variance
Example from M5Stack: https://github.com/m5stack/UIFlow-Code/wiki/Unit#tof
"""

from m5stack import lcd
from m5ui import M5TextBox, M5Title, setScreenColor
from uiflow import wait_ms
import time
import unit
import math

lcd.clear()
lcd.setRotation(3)
distfield = M5TextBox(40, 20, "0", lcd.FONT_DejaVu40, 0x08feab)
distlabel = M5TextBox(0, 0, "M5StickC VL53L0X", lcd.FONT_Small, 0xFFFFFF)

tof = unit.get(unit.TOF, unit.PORTA)

def mean(element):
    sumUnit = 0
    for x in element:
        sumUnit += x

    return sumUnit/len(element)

def variance(element):
    meanUnit = mean(element)
    variance = 0

    for x in element:
        variance += (x - meanUnit)**2

    variance = variance/(len(element) - 1)
    return variance

def stdev(element):
    return math.sqrt(variance(element))

numReadings = []

while True:
    for i in range(60):
        distfield.setText(str(tof.distance))
        delta_tof = 1 + (tof.distance*3//100)
        mmlabel.setText("+/- " + str(delta_tof) + " mm")
        numReadings.append(tof.distance)
        wait_ms(75)
    print("MicroPython v1.11-321; ESP32 module with ESP32 - M5StickC VL53L0X Unit: Statistics distance")
    print("Mean = {:.3f} mm, Variance = {:.3f}, Standard deviation = {:.3f} \n \n".format(mean(numReadings), variance(numReadings), stdev(numReadings)))
    numReadings = []
