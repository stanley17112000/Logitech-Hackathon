import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


# LED snippets
##############

# Set all device lighting to red
from logipy import logi_led
import time
import ctypes

class light:
	def __init__(self):
		logi_led.logi_led_init()
		self.line = [  
				#L
                logi_led.F2,
                logi_led.TWO,
                logi_led.Q,
                logi_led.CAPS_LOCK,
                logi_led.Z,
                logi_led.LEFT_SHIFT,
                #I
                logi_led.F5,
                logi_led.F6,
                logi_led.F7,
                logi_led.SEVEN,
                logi_led.Y,
                logi_led.G,
                logi_led.C,
                logi_led.V,
                logi_led.B,
                #N
                logi_led.F9,
                logi_led.F12,
                logi_led.ZERO,
                logi_led.O,
                logi_led.K,
                logi_led.M,
                logi_led.MINUS,
                logi_led.OPEN_BRACKET,
                logi_led.FORWARD_SLASH,
                logi_led.APOSTROPHE,
                logi_led.CLOSE_BRACKET,
                logi_led.BACKSPACE,
                #E
                logi_led.NUM_LOCK,
                logi_led.NUM_SLASH,
                logi_led.NUM_ASTERISK,
                logi_led.NUM_SEVEN,
                logi_led.NUM_FOUR,
                logi_led.NUM_FIVE,
                logi_led.NUM_SIX,
                logi_led.NUM_ONE,
                logi_led.NUM_ZERO,
                logi_led.NUM_PERIOD ]
		self.facebook = [  
				#F
                logi_led.F2,
                logi_led.F3,
                logi_led.F4,
                logi_led.THREE,
                logi_led.D,
                logi_led.C,
                logi_led.E,
                logi_led.R,
                logi_led.T,
                #B
                logi_led.F5,
                logi_led.F6,
                logi_led.F7,
                logi_led.SEVEN,
                logi_led.U,
                logi_led.J,
                logi_led.M,
                logi_led.COMMA,
                logi_led.PERIOD,
                logi_led.FORWARD_SLASH,
                logi_led.NINE,
                logi_led.I,
                logi_led.O,
                logi_led.P,
                logi_led.SEMICOLON, ]

	def line_led(self):
		logi_led.logi_led_set_lighting(0, 0, 0)
		for i in self.line:
			logi_led.logi_led_flash_single_key(i, 0, 100, 0, 5000, 50)

	def facebook_led(self):
		logi_led.logi_led_set_lighting(0, 0, 0)
		for i in self.facebook:
			logi_led.logi_led_flash_single_key(i, 0, 0, 100, 5000, 50)

if __name__ == '__main__':
	Light = light()

	print ('Setting all device lighting to Line...')
	time.sleep(1) # Give the SDK a second to initialize
	Light.line_led()
	time.sleep(5)

	print ('Setting all device lighting to FB...')
	time.sleep(1) # Give the SDK a second to initialize
	Light.facebook_led()
	time.sleep(5)

