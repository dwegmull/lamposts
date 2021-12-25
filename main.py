# Trinket IO demo
# Welcome to CircuitPython 3.1.1 :)

import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
import touchio
#from adafruit_hid.keyboard import Keyboard
#from adafruit_hid.keycode import Keycode
#import adafruit_dotstar as dotstar
import time
import neopixel

# One pixel connected internally!
#dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

# Built in red LED
#led = DigitalInOut(board.D13)
#led.direction = Direction.OUTPUT

# Analog input on D0
#analog1in = AnalogIn(board.D0)

# Analog output on D1
#aout = AnalogOut(board.D1)

# Digital input with pullup on D2
button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Capacitive touch on D1, D3 and D4
touch1 = touchio.TouchIn(board.D1)
touch3 = touchio.TouchIn(board.D3)
touch4 = touchio.TouchIn(board.D4)


# NeoPixel strip (of 16 LEDs) connected on D4
NUMPIXELS = 44
neopixels = neopixel.NeoPixel(board.D13, NUMPIXELS, brightness=1, auto_write=False)

# Used if we do HID output, see below
#kbd = Keyboard()
ledMode = 0
brightness = 255
modeSwitch = 0
######################### HELPERS ##############################



def updateMode(brightness):
  print("updating to", ledMode, brightness)
  for p in range(NUMPIXELS):
      if ledMode == 0:
        #                         G                              R                           B
        neopixels[p] = (int((brightness * 255) / 256), int((brightness * 255) / 256), int((brightness * 255) / 256))
      elif ledMode == 1:
        neopixels[p] = (int((brightness * 197) / 256), int((brightness * 255) / 256), int((brightness * 143) / 256))
      elif ledMode == 2:
        neopixels[p] = (int((brightness * 50) / 256), int((brightness * 255) / 256), int((brightness * 41) / 256))
      elif ledMode == 3:
        neopixels[p] = (int((brightness * 183) / 256), int((brightness * 255) / 256), int((brightness * 76) / 256))
      else:
        neopixels[p] = (0, 0, 0)
  neopixels.show()

######################### MAIN LOOP ##############################

updateMode(brightness)
while True:
  
  if touch1.value and (modeSwitch == 0):
      print("D1 touched!")
      modeSwitch = 1
      ledMode = ledMode + 1
      if ledMode > 4:
        ledMode = 0
      updateMode(brightness)
  elif touch3.value:
      print("D3 touched!")
      if brightness > 10:
        brightness = brightness - 10
        updateMode(brightness)
  elif touch4.value:
      print("D4 touched!")
      if brightness < 245:
        brightness = brightness + 10
        updateMode(brightness)

  if (touch1.value == 0) and (modeSwitch == 1):
    modeSwitch = 0
    print("modeSwitch back to 0")


