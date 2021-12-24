This code is meant to run on an Adafruit Trinket M0 with CircuitPython.
It drives a 44 string of Neopixels which are mounted on a circular board.
It requires the following hardware modifications:
1. Remove the series resistor that connects PIN 13 to the red LED. This pin is the only available one that can drive the LEDs as the deafult one is used as a touch input.
2. Pins D1, D3 and D4 are touch inputs that control the mode, brightness down, brightness up, respectively.
The LEDs must be powered at 4.5V so the 3.3V signal from the Trinket will be above the high logic threshold of the Neopixel (specified as 3.5V with a 5V supply which I assume is actually 0.7 * 5 which is a common threshold for CMOS chips).
