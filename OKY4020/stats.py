#!/usr/bin/python3

import time

import adafruit_ssd1306
import busio

from board import SCL, SDA
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# 128x64 display with hardware I2C:
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear the display.  Always call show after changing pixels to make the display
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('PixelOperator.ttf', 16)

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Get stats
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    temp = subprocess.check_output(cmd, shell = True )

    # Write stats
    draw.text((x, top+2),       "IP: " + str(IP, 'utf-8'),  font=font, fill=255)
    draw.text((x, top+18),     str(CPU, 'utf-8') + " " + str(temp, 'utf-8'), font=font, fill=255)
    draw.text((x, top+34),    str(MemUsage, 'utf-8'),  font=font, fill=255)
    draw.text((x, top+50),    str(Disk, 'utf-8'),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(.1)
