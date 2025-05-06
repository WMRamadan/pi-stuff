# OKY4020 OLED Display Stats Script

This is a script for displaying Pi stats such as (IP, CPU Load, CPU Temp, RAM, Disk) on the OKY4020 display.

## Requirements:
- Python3
- Pip3
- I2C Enabled
- Pillow
- Adafruit-SSD1306

## Setup:

**Step 1** - Clone the repository to your Raspberry Pi home directory.
```bash
git clone  https://github.com/WMRamadan/pi-stuff.git
```

**Step 2** - Make sure that you have the display connected correctly and that all necessary libraries are installed. Then add the line in the `cron` file to your cronjob using `crontab -e` and make sure to change the paths to the correct paths that correspond to your setup.

**Step 3** - Reboot your Raspberry Pi and the script should start working once it is fully booted. You can also test the script before boot by simply running the python script. The cronjob will make sure that it is loaded on each reboot.
