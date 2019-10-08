import time
import random
from gfxhat import lcd
import gfxhat

#function to randomly put pixel on gfxhat for 2 seconds
def pixelrain():
    endprogram = time.time() + 2
    while time.time() < endprogram:
        x = random.randint(0,127)
        y = random.randint(0,63)
        lcd.set_pixel(x,y,1)

#function to make staircase from given point on gfxhat
def staircase(x,y,w=10,l=10) :
    indexY= y-l
    indexX = x-w
    while indexX >= w and indexY >= l:
        while x >= indexX:
            lcd.set_pixel(x,y,1)
            x -=1

        while y>= indexY:
            lcd.set_pixel(x,y,1)
            y -=1

    lcd.show


#Function to make verticle line at given point on gfxhat
def verticleLine(x) :
    y = 0
    while(y<64) :
        lcd.set_pixel(x,y,1)
        x +=1

    lcd.show()


#Function to make horizontal line at given point on gfxhat
def horizontalLine(y) :
    x = 0
    while(x<128) :
        lcd.set_pixel(x,y,1)
        x +=1

    lcd.show()


#Function to reset backlight colour for gfxhat
def clearBacklight():
    gfxhat.lcd.clear()
    gfxhat.backlight.setall(0,0,0)
    gfxhat.backlight.setall(50,50,50)
    gfx.backlight.show()
