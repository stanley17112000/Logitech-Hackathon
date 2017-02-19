import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# LED snippets
##############

# Set all device lighting to red
from logipy import logi_led
import time
import ctypes

keyTObit = {}
keyTObit[logi_led.ESC] = 0
keyTObit[logi_led.F1] = 4
keyTObit[logi_led.F2] = 8
keyTObit[logi_led.F3] = 12
keyTObit[logi_led.F4] = 16
keyTObit[logi_led.F5] = 20
keyTObit[logi_led.F6] = 24
keyTObit[logi_led.F7] = 28
keyTObit[logi_led.F8] = 32
keyTObit[logi_led.F9] = 36
keyTObit[logi_led.F10] = 40
keyTObit[logi_led.F11] = 44
keyTObit[logi_led.F12] = 48
keyTObit[logi_led.PRINT_SCREEN] = 52
keyTObit[logi_led.SCROLL_LOCK] = 56
keyTObit[logi_led.PAUSE_BREAK] = 60

keyTObit[logi_led.TILDE] = 0+21*4*1
keyTObit[logi_led.ONE] = 4+21*4*1
keyTObit[logi_led.TWO] = 8+21*4*1
keyTObit[logi_led.THREE] = 12+21*4*1
keyTObit[logi_led.FOUR] = 16+21*4*1
keyTObit[logi_led.FIVE] = 20+21*4*1
keyTObit[logi_led.SIX] = 24+21*4*1
keyTObit[logi_led.SEVEN] = 28+21*4*1
keyTObit[logi_led.EIGHT] = 32+21*4*1
keyTObit[logi_led.NINE] = 36+21*4*1
keyTObit[logi_led.ZERO] = 40+21*4*1
keyTObit[logi_led.MINUS] = 44+21*4*1
keyTObit[logi_led.EQUALS] = 48+21*4*1
keyTObit[logi_led.BACKSPACE] = 52+21*4*1
keyTObit[logi_led.INSERT] = 56+21*4*1
keyTObit[logi_led.HOME] = 60+21*4*1
keyTObit[logi_led.PAGE_UP] = 64+21*4*1
keyTObit[logi_led.NUM_LOCK] = 68+21*4*1
keyTObit[logi_led.NUM_SLASH] = 72+21*4*1
keyTObit[logi_led.NUM_ASTERISK] = 76+21*4*1
keyTObit[logi_led.NUM_MINUS] = 80+21*4*1

keyTObit[logi_led.TAB] = 0+21*4*2
keyTObit[logi_led.Q] = 4+21*4*2
keyTObit[logi_led.W] = 8+21*4*2
keyTObit[logi_led.E] = 12+21*4*2
keyTObit[logi_led.R] = 16+21*4*2
keyTObit[logi_led.T] = 20+21*4*2
keyTObit[logi_led.Y] = 24+21*4*2
keyTObit[logi_led.U] = 28+21*4*2
keyTObit[logi_led.I] = 32+21*4*2
keyTObit[logi_led.O] = 36+21*4*2
keyTObit[logi_led.P] = 40+21*4*2
keyTObit[logi_led.OPEN_BRACKET] = 44+21*4*2
keyTObit[logi_led.CLOSE_BRACKET] = 48+21*4*2
keyTObit[logi_led.BACKSLASH] = 52+21*4*2
keyTObit[logi_led.KEYBOARD_DELETE] = 56+21*4*2
keyTObit[logi_led.END] = 60+21*4*2
keyTObit[logi_led.PAGE_DOWN] = 64+21*4*2
keyTObit[logi_led.NUM_SEVEN] = 68+21*4*2
keyTObit[logi_led.NUM_EIGHT] = 72+21*4*2
keyTObit[logi_led.NUM_NINE] = 76+21*4*2
keyTObit[logi_led.NUM_PLUS] = 80+21*4*2

keyTObit[logi_led.CAPS_LOCK] = 0+21*4*3
keyTObit[logi_led.A] = 4+21*4*3
keyTObit[logi_led.S] = 8+21*4*3
keyTObit[logi_led.D] = 12+21*4*3
keyTObit[logi_led.F] = 16+21*4*3
keyTObit[logi_led.G] = 20+21*4*3
keyTObit[logi_led.H] = 24+21*4*3
keyTObit[logi_led.J] = 28+21*4*3
keyTObit[logi_led.K] = 32+21*4*3
keyTObit[logi_led.L] = 36+21*4*3
keyTObit[logi_led.SEMICOLON] = 40+21*4*3
keyTObit[logi_led.APOSTROPHE] = 44+21*4*3
keyTObit[logi_led.ENTER] = 52+21*4*3
keyTObit[logi_led.NUM_FOUR] = 68+21*4*3
keyTObit[logi_led.NUM_FIVE] = 72+21*4*3
keyTObit[logi_led.NUM_SIX] = 76+21*4*3

keyTObit[logi_led.LEFT_SHIFT] = 0+21*4*4
keyTObit[logi_led.Z] = 8+21*4*4
keyTObit[logi_led.X] = 12+21*4*4
keyTObit[logi_led.C] = 16+21*4*4
keyTObit[logi_led.V] = 20+21*4*4
keyTObit[logi_led.B] = 24+21*4*4
keyTObit[logi_led.N] = 28+21*4*4
keyTObit[logi_led.M] = 32+21*4*4
keyTObit[logi_led.COMMA] = 36+21*4*4
keyTObit[logi_led.PERIOD] = 40+21*4*4
keyTObit[logi_led.FORWARD_SLASH] = 44+21*4*4
keyTObit[logi_led.RIGHT_SHIFT] = 52+21*4*4
keyTObit[logi_led.ARROW_UP] = 60+21*4*4
keyTObit[logi_led.NUM_ONE] = 68+21*4*4
keyTObit[logi_led.NUM_TWO] = 72+21*4*4
keyTObit[logi_led.NUM_THREE] = 76+21*4*4
keyTObit[logi_led.NUM_ENTER] = 80+21*4*4

keyTObit[logi_led.LEFT_CONTROL] = 0+21*4*5
keyTObit[logi_led.LEFT_WINDOWS] = 4+21*4*5
keyTObit[logi_led.LEFT_ALT] = 8+21*4*5
keyTObit[logi_led.SPACE] = 20+21*4*5
keyTObit[logi_led.RIGHT_ALT] = 44+21*4*5
keyTObit[logi_led.RIGHT_WINDOWS] = 48+21*4*5
keyTObit[logi_led.APPLICATION_SELECT] = 52+21*4*5
keyTObit[logi_led.RIGHT_CONTROL] = 56+21*4*5
keyTObit[logi_led.ARROW_LEFT] = 60+21*4*5
keyTObit[logi_led.ARROW_DOWN] = 64+21*4*5
keyTObit[logi_led.ARROW_RIGHT] = 68+21*4*5
keyTObit[logi_led.NUM_ZERO] = 72+21*4*5
keyTObit[logi_led.NUM_PERIOD] = 76+21*4*5

keyTObit[logi_led.G_1] = 0+21*4*6
keyTObit[logi_led.G_2] = 4+21*4*6
keyTObit[logi_led.G_3] = 8+21*4*6
keyTObit[logi_led.G_4] = 12+21*4*6
keyTObit[logi_led.G_5] = 16+21*4*6
keyTObit[logi_led.G_6] = 20+21*4*6
keyTObit[logi_led.G_7] = 24+21*4*6
keyTObit[logi_led.G_8] = 28+21*4*6
keyTObit[logi_led.G_9] = 32+21*4*6
keyTObit[logi_led.G_LOGO] = 36+21*4*6
keyTObit[logi_led.G_BADGE] = 40+21*4*6



class light:
	def __init__(self):
		logi_led.logi_led_init()
                self.bitmap_line = [chr(0),chr(0),chr(0),chr(255)]*21*7
                self.bitmap_facebook = [chr(0),chr(0),chr(0),chr(255)]*21*7
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

                # for i in range(0, 21 * 7 * 4, 4):
                #         self.bitmap_line[i + 0] = chr(0)
                #         self.bitmap_line[i + 1] = chr(0)
                #         self.bitmap_line[i + 2] = chr(255)
                #         self.bitmap_facebook[i + 0] = chr(9)
                #         self.bitmap_facebook[i + 1] = chr(58)
                #         self.bitmap_facebook[i + 2] = chr(255)

                for i in self.line:
                        self.bitmap_line[ keyTObit[i] + 0 ] = chr(0)
                        self.bitmap_line[ keyTObit[i] + 1 ] = chr(255)
                        self.bitmap_line[ keyTObit[i] + 2 ] = chr(0)
                        self.bitmap_line[ keyTObit[i] + 3 ] = chr(255)

                for i in self.facebook:
                        self.bitmap_facebook[ keyTObit[i] + 0 ] = chr(255)
                        self.bitmap_facebook[ keyTObit[i] + 1 ] = chr(0)
                        self.bitmap_facebook[ keyTObit[i] + 2 ] = chr(0)
                        self.bitmap_facebook[ keyTObit[i] + 3 ] = chr(255)
                self.line_str = "".join(self.bitmap_line)
                self.facebook_str = "".join(self.bitmap_facebook)

	def line_led(self, times, intval):
                logi_led.logi_led_save_current_lighting()
                time.sleep(0.1)
                for i in range(0, times):
                        logi_led.logi_led_set_lighting(0, 0, 0)
                        time.sleep(intval / 2)
        		logi_led.logi_led_set_lighting_from_bitmap(self.line_str)
                        time.sleep(intval / 2)
                logi_led.logi_led_stop_effects()
                logi_led.logi_led_restore_lighting()

	def facebook_led(self, times, intval):
		logi_led.logi_led_set_lighting(0, 0, 0)
                time.sleep(0.1)
                for i in range(0, times):
                        logi_led.logi_led_set_lighting(0, 0, 0)
                        time.sleep(intval / 2)
                        logi_led.logi_led_set_lighting_from_bitmap(self.facebook_str)
                        time.sleep(intval / 2)
                logi_led.logi_led_stop_effects()
                logi_led.logi_led_restore_lighting()

if __name__ == '__main__':
	Light = light()

	print ('Setting all device lighting to Line...')
	time.sleep(1) # Give the SDK a second to initialize
	Light.line_led(10, 10)
	time.sleep(5)

	print ('Setting all device lighting to FB...')
	time.sleep(1) # Give the SDK a second to initialize
	Light.facebook_led(10, 10)
	time.sleep(5)

