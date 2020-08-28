# M5StickC VL53L0X Hat v0.0.2 - 12/01/2020
# Example from M5Stack : https://github.com/m5stack/UIFlow-Code/wiki/Unit#tof

from m5stack import lcd
from m5ui import M5TextBox, M5Title, setScreenColor
from uiflow import wait_ms
import time
import hat

lcd.clear()
lcd.setRotation(3)
distfield = M5TextBox(40, 20, "0", lcd.FONT_DejaVu40, 0x08feab)
mmlabel = M5TextBox(70, 64, "+/- 3 mm", lcd.FONT_Default, 0xFFFFFF)
distlabel = M5TextBox(0, 0, "M5Stick VL53L0X Hat", lcd.FONT_Small, 0xFFFFFF)

tof = hat.get(hat.TOF)

while True:
    distfield.setText(str(tof.GetDistance()))
    delta_tof = 1 + (tof.GetDistance()*3//100)
    mmlabel.setText("+/- " + str(delta_tof) + " mm")
    print('(' + str(tof.GetDistance()) + " +/- " + str(delta_tof) + ") mm")
    wait_ms(75)

