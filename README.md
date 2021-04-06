# serial-control-led-strip
The principle idea is to control effects of an LED strip (e.g. WS2812B) from the terminal of a PC.
Hence, a microcontroler has to be used, to act as communicator between PC and LED strip.

![Arduino schematics (part 1/2)](https://github.com/ernestkrom/serial-control-led-strip/blob/main/documentation/png/schematics_1.png)

![Arduino schematics (part 2/2)](https://github.com/ernestkrom/serial-control-led-strip/blob/main/documentation/png/schematics_2.png)

Steps:
1. Wire up Arduino as depicted above
2. Flash the microcontroller with the .ino file
3. Run the Python script from a terminal (edit USB port beforehand)

Dependencies:
* Arduino IDE installed, and "Adafruit NeoPixel Library" added
* Python 3.x installed, and added to path variable
* "pip install serial" executed (Python library for serial communication)

Windows-specific:
* Install Python 3.x and add to PATH
* python -m pip install pyserial
* Install driver for Arduino: https://sparks.gogo.co.nz/ch340.html
