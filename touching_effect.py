import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


# LED snippets
##############
# Set all device lighting to red
from logipy import logi_led
import time
import ctypes

import random


val = logi_led.logi_led_init()
print "init = ",val
time.sleep(1) # Give the SDK a second to initialize

neighbor = {}
neighbor[logi_led.ESC] = [logi_led.G_LOGO, logi_led.F1, logi_led.ONE, logi_led.TILDE, logi_led.G_1]
neighbor[logi_led.F1] = [logi_led.G_6, logi_led.G_7, logi_led.ESC, logi_led.F2, logi_led.ONE, logi_led.TWO]
neighbor[logi_led.F2] = [logi_led.G_6, logi_led.G_7, logi_led.G_8, logi_led.F1, logi_led.F3, logi_led.TWO, logi_led.THREE]
neighbor[logi_led.F3] = [logi_led.G_7, logi_led.G_8, logi_led.G_9, logi_led.F2, logi_led.F4, logi_led.THREE, logi_led.FOUR]
neighbor[logi_led.F4] = [logi_led.G_8, logi_led.G_9, logi_led.F3, logi_led.F5, logi_led.FOUR, logi_led.FIVE]
neighbor[logi_led.F5] = [logi_led.F4, logi_led.F6, logi_led.FIVE, logi_led.SIX, logi_led.SEVEN]
neighbor[logi_led.F6] = [logi_led.F5, logi_led.F7, logi_led.SEVEN, logi_led.EIGHT]
neighbor[logi_led.F7] = [logi_led.F6, logi_led.F8, logi_led.EIGHT, logi_led.NINE]
neighbor[logi_led.F8] = [logi_led.F7, logi_led.F9, logi_led.NINE, logi_led.ZERO]
neighbor[logi_led.F9] = [logi_led.F8, logi_led.F10, logi_led.ZERO, logi_led.MINUS, logi_led.EQUALS]
neighbor[logi_led.F10] = [logi_led.F9, logi_led.F11, logi_led.MINUS, logi_led.EQUALS]
neighbor[logi_led.F11] = [logi_led.F10, logi_led.F12, logi_led.EQUALS, logi_led.BACKSPACE]
neighbor[logi_led.F12] = [logi_led.F11, logi_led.PRINT_SCREEN, logi_led.BACKSPACE]
neighbor[logi_led.PRINT_SCREEN] = [logi_led.F12, logi_led.SCROLL_LOCK, logi_led.INSERT, logi_led.HOME]
neighbor[logi_led.SCROLL_LOCK] = [logi_led.PRINT_SCREEN, logi_led.PAUSE_BREAK, logi_led.INSERT, logi_led.HOME, logi_led.PAGE_UP]
neighbor[logi_led.PAUSE_BREAK] = [logi_led.SCROLL_LOCK, logi_led.HOME, logi_led.PAGE_UP, logi_led.NUM_LOCK]

neighbor[logi_led.TILDE] = [logi_led.G_LOGO, logi_led.ESC, logi_led.G_1, logi_led.ONE, logi_led.G_2, logi_led.TAB]
neighbor[logi_led.ONE] = [logi_led.ESC, logi_led.F1, logi_led.TILDE, logi_led.TWO, logi_led.TAB, logi_led.Q]
neighbor[logi_led.TWO] = [logi_led.F1, logi_led.F2, logi_led.ONE, logi_led.THREE, logi_led.Q, logi_led.W]
neighbor[logi_led.THREE] = [logi_led.F2, logi_led.F3, logi_led.TWO, logi_led.FOUR, logi_led.W, logi_led.E]
neighbor[logi_led.FOUR] = [logi_led.F3, logi_led.F4, logi_led.THREE, logi_led.FIVE, logi_led.E, logi_led.R]
neighbor[logi_led.FIVE] = [logi_led.F4, logi_led.FOUR, logi_led.SIX, logi_led.R, logi_led.T]
neighbor[logi_led.SIX] = [logi_led.F5, logi_led.FIVE, logi_led.SEVEN, logi_led.T, logi_led.Y]
neighbor[logi_led.SEVEN] = [logi_led.F5, logi_led.F6, logi_led.SIX, logi_led.EIGHT, logi_led.Y, logi_led.U]
neighbor[logi_led.EIGHT] = [logi_led.F6, logi_led.F7, logi_led.SEVEN, logi_led.NINE, logi_led.U, logi_led.I]
neighbor[logi_led.NINE] = [logi_led.F7, logi_led.F8, logi_led.EIGHT, logi_led.ZERO, logi_led.I, logi_led.O]
neighbor[logi_led.ZERO] = [logi_led.F8, logi_led.F9, logi_led.NINE, logi_led.MINUS, logi_led.O, logi_led.P]
neighbor[logi_led.MINUS] = [logi_led.F9, logi_led.F10, logi_led.ZERO, logi_led.EQUALS, logi_led.P, logi_led.OPEN_BRACKET]
neighbor[logi_led.EQUALS] = [logi_led.F10, logi_led.F11, logi_led.MINUS, logi_led.BACKSPACE, logi_led.OPEN_BRACKET, logi_led.CLOSE_BRACKET]
neighbor[logi_led.BACKSPACE] = [logi_led.F11, logi_led.F12, logi_led.EQUALS, logi_led.INSERT, logi_led.CLOSE_BRACKET, logi_led.BACKSLASH]
neighbor[logi_led.INSERT] = [logi_led.F12, logi_led.PRINT_SCREEN, logi_led.SCROLL_LOCK, logi_led.BACKSPACE, logi_led.HOME, logi_led.BACKSLASH, logi_led.KEYBOARD_DELETE, logi_led.END]
neighbor[logi_led.HOME] = [logi_led.PRINT_SCREEN, logi_led.SCROLL_LOCK, logi_led.PAUSE_BREAK, logi_led.INSERT, logi_led.PAGE_UP, logi_led.KEYBOARD_DELETE, logi_led.END, logi_led.PAGE_DOWN]
neighbor[logi_led.PAGE_UP] = [logi_led.SCROLL_LOCK, logi_led.PAUSE_BREAK, logi_led.HOME, logi_led.NUM_LOCK, logi_led.END, logi_led.PAGE_DOWN]
neighbor[logi_led.NUM_LOCK] = [logi_led.PAUSE_BREAK, logi_led.PAGE_UP, logi_led.NUM_SLASH, logi_led.PAGE_DOWN, logi_led.NUM_SEVEN, logi_led.NUM_EIGHT]
neighbor[logi_led.NUM_SLASH] = [logi_led.NUM_LOCK, logi_led.NUM_ASTERISK, logi_led.NUM_SEVEN, logi_led.NUM_EIGHT, logi_led.NUM_NINE]
neighbor[logi_led.NUM_ASTERISK] = [logi_led.NUM_SLASH, logi_led.NUM_MINUS, logi_led.NUM_EIGHT, logi_led.NUM_NINE, logi_led.NUM_PLUS]
neighbor[logi_led.NUM_MINUS] = [logi_led.NUM_ASTERISK, logi_led.NUM_NINE, logi_led.NUM_PLUS]

neighbor[logi_led.TAB] = [logi_led.G_1, logi_led.TILDE, logi_led.ONE, logi_led.G_2, logi_led.Q, logi_led.G_3, logi_led.CAPS_LOCK]
neighbor[logi_led.Q] = [logi_led.ONE, logi_led.TWO, logi_led.TAB, logi_led.W, logi_led.CAPS_LOCK, logi_led.A]
neighbor[logi_led.W] = [logi_led.TWO, logi_led.THREE, logi_led.Q, logi_led.E, logi_led.A, logi_led.S]
neighbor[logi_led.E] = [logi_led.THREE, logi_led.FOUR, logi_led.W, logi_led.R, logi_led.S, logi_led.D]
neighbor[logi_led.R] = [logi_led.FOUR, logi_led.FIVE, logi_led.E, logi_led.T, logi_led.D, logi_led.F]
neighbor[logi_led.T] = [logi_led.FIVE, logi_led.SIX, logi_led.R, logi_led.Y, logi_led.F, logi_led.G]
neighbor[logi_led.Y] = [logi_led.SIX, logi_led.SEVEN, logi_led.T, logi_led.U, logi_led.G, logi_led.H]
neighbor[logi_led.U] = [logi_led.SEVEN, logi_led.EIGHT, logi_led.Y, logi_led.I, logi_led.H, logi_led.J]
neighbor[logi_led.I] = [logi_led.EIGHT, logi_led.NINE, logi_led.U, logi_led.O, logi_led.J, logi_led.K]
neighbor[logi_led.O] = [logi_led.NINE, logi_led.ZERO, logi_led.I, logi_led.P, logi_led.K, logi_led.L]
neighbor[logi_led.P] = [logi_led.ZERO, logi_led.MINUS, logi_led.O, logi_led.OPEN_BRACKET, logi_led.L, logi_led.SEMICOLON]
neighbor[logi_led.OPEN_BRACKET] = [logi_led.MINUS, logi_led.EQUALS, logi_led.P, logi_led.CLOSE_BRACKET, logi_led.SEMICOLON, logi_led.APOSTROPHE]
neighbor[logi_led.CLOSE_BRACKET] = [logi_led.EQUALS, logi_led.BACKSPACE, logi_led.OPEN_BRACKET, logi_led.BACKSLASH, logi_led.APOSTROPHE, logi_led.ENTER]
neighbor[logi_led.BACKSLASH] = [logi_led.BACKSPACE, logi_led.INSERT, logi_led.CLOSE_BRACKET, logi_led.KEYBOARD_DELETE, logi_led.ENTER]
neighbor[logi_led.KEYBOARD_DELETE] = [logi_led.INSERT, logi_led.HOME, logi_led.BACKSLASH, logi_led.END]
neighbor[logi_led.END] = [logi_led.INSERT, logi_led.HOME, logi_led.PAGE_UP, logi_led.KEYBOARD_DELETE, logi_led.PAGE_DOWN]
neighbor[logi_led.PAGE_DOWN] = [logi_led.HOME, logi_led.PAGE_UP, logi_led.NUM_LOCK, logi_led.END, logi_led.NUM_SEVEN, logi_led.NUM_FOUR]
neighbor[logi_led.NUM_SEVEN] = [logi_led.PAGE_UP, logi_led.NUM_LOCK, logi_led.NUM_SLASH, logi_led.PAGE_DOWN, logi_led.NUM_EIGHT, logi_led.NUM_FOUR, logi_led.NUM_FIVE]
neighbor[logi_led.NUM_EIGHT] = [logi_led.NUM_LOCK, logi_led.NUM_SLASH, logi_led.NUM_ASTERISK, logi_led.NUM_SEVEN, logi_led.NUM_NINE, logi_led.NUM_FOUR, logi_led.NUM_FIVE, logi_led.NUM_SIX]
neighbor[logi_led.NUM_NINE] = [logi_led.NUM_SLASH, logi_led.NUM_ASTERISK, logi_led.NUM_MINUS, logi_led.NUM_EIGHT, logi_led.NUM_PLUS, logi_led.NUM_FIVE, logi_led.NUM_SIX]
neighbor[logi_led.NUM_PLUS] = [logi_led.NUM_ASTERISK, logi_led.NUM_MINUS, logi_led.NUM_NINE, logi_led.NUM_SIX, logi_led.NUM_THREE, logi_led.NUM_ENTER]

neighbor[logi_led.CAPS_LOCK] = [logi_led.G_2, logi_led.TAB, logi_led.Q, logi_led.G_3, logi_led.A, logi_led.G_4, logi_led.LEFT_SHIFT]
neighbor[logi_led.A] = [logi_led.Q, logi_led.W, logi_led.CAPS_LOCK, logi_led.S, logi_led.LEFT_SHIFT, logi_led.Z]
neighbor[logi_led.S] = [logi_led.W, logi_led.E, logi_led.A, logi_led.D, logi_led.Z, logi_led.X]
neighbor[logi_led.D] = [logi_led.E, logi_led.R, logi_led.S, logi_led.F, logi_led.X, logi_led.C]
neighbor[logi_led.F] = [logi_led.R, logi_led.T, logi_led.D, logi_led.G, logi_led.C, logi_led.V]
neighbor[logi_led.G] = [logi_led.T, logi_led.Y, logi_led.F, logi_led.H, logi_led.V, logi_led.B]
neighbor[logi_led.H] = [logi_led.Y, logi_led.U, logi_led.G, logi_led.J, logi_led.B, logi_led.N]
neighbor[logi_led.J] = [logi_led.U, logi_led.I, logi_led.H, logi_led.K, logi_led.N, logi_led.M]
neighbor[logi_led.K] = [logi_led.I, logi_led.O, logi_led.J, logi_led.L, logi_led.M, logi_led.COMMA]
neighbor[logi_led.L] = [logi_led.O, logi_led.P, logi_led.K, logi_led.SEMICOLON, logi_led.COMMA, logi_led.PERIOD]
neighbor[logi_led.SEMICOLON] = [logi_led.P, logi_led.OPEN_BRACKET, logi_led.L, logi_led.APOSTROPHE, logi_led.PERIOD, logi_led.FORWARD_SLASH]
neighbor[logi_led.APOSTROPHE] = [logi_led.OPEN_BRACKET, logi_led.CLOSE_BRACKET, logi_led.SEMICOLON, logi_led.ENTER, logi_led.FORWARD_SLASH, logi_led.RIGHT_SHIFT]
neighbor[logi_led.ENTER] = [logi_led.CLOSE_BRACKET, logi_led.BACKSLASH, logi_led.APOSTROPHE, logi_led.RIGHT_SHIFT]
neighbor[logi_led.NUM_FOUR] = [logi_led.PAGE_DOWN, logi_led.NUM_SEVEN, logi_led.NUM_EIGHT, logi_led.NUM_FIVE, logi_led.NUM_ONE, logi_led.NUM_TWO]
neighbor[logi_led.NUM_FIVE] = [logi_led.NUM_SEVEN, logi_led.NUM_EIGHT, logi_led.NUM_NINE, logi_led.NUM_FOUR, logi_led.NUM_SIX, logi_led.NUM_ONE, logi_led.NUM_TWO, logi_led.NUM_THREE]
neighbor[logi_led.NUM_SIX] = [logi_led.NUM_EIGHT, logi_led.NUM_NINE, logi_led.NUM_PLUS, logi_led.NUM_FIVE, logi_led.NUM_TWO, logi_led.NUM_THREE, logi_led.NUM_ENTER]

neighbor[logi_led.LEFT_SHIFT] = [logi_led.G_3, logi_led.CAPS_LOCK, logi_led.A, logi_led.G_4, logi_led.Z, logi_led.LEFT_CONTROL, logi_led.LEFT_WINDOWS]
neighbor[logi_led.Z] = [logi_led.A, logi_led.S, logi_led.LEFT_SHIFT, logi_led.X, logi_led.LEFT_WINDOWS, logi_led.LEFT_ALT]
neighbor[logi_led.X] = [logi_led.S, logi_led.D, logi_led.Z, logi_led.C, logi_led.LEFT_ALT]
neighbor[logi_led.C] = [logi_led.D, logi_led.F, logi_led.X, logi_led.V]
neighbor[logi_led.V] = [logi_led.F, logi_led.G, logi_led.C, logi_led.B]
neighbor[logi_led.B] = [logi_led.G, logi_led.H, logi_led.V, logi_led.N, logi_led.SPACE]
neighbor[logi_led.N] = [logi_led.H, logi_led.J, logi_led.B, logi_led.M, logi_led.SPACE]
neighbor[logi_led.M] = [logi_led.J, logi_led.K, logi_led.N, logi_led.COMMA]
neighbor[logi_led.COMMA] = [logi_led.K, logi_led.L, logi_led.M, logi_led.PERIOD, logi_led.RIGHT_ALT]
neighbor[logi_led.PERIOD] = [logi_led.L, logi_led.SEMICOLON, logi_led.COMMA, logi_led.FORWARD_SLASH, logi_led.RIGHT_ALT, logi_led.RIGHT_WINDOWS]
neighbor[logi_led.FORWARD_SLASH] = [logi_led.SEMICOLON, logi_led.APOSTROPHE, logi_led.PERIOD, logi_led.RIGHT_SHIFT, logi_led.RIGHT_WINDOWS, logi_led.APPLICATION_SELECT]
neighbor[logi_led.RIGHT_SHIFT] = [logi_led.APOSTROPHE, logi_led.ENTER, logi_led.FORWARD_SLASH, logi_led.APPLICATION_SELECT, logi_led.RIGHT_CONTROL]
neighbor[logi_led.ARROW_UP] = [logi_led.ARROW_LEFT, logi_led.ARROW_DOWN, logi_led.ARROW_RIGHT]
neighbor[logi_led.NUM_ONE] = [logi_led.NUM_FOUR, logi_led.NUM_FIVE, logi_led.NUM_TWO, logi_led.ARROW_RIGHT, logi_led.NUM_ZERO]
neighbor[logi_led.NUM_TWO] = [logi_led.NUM_FOUR, logi_led.NUM_FIVE, logi_led.NUM_SIX, logi_led.NUM_ONE, logi_led.NUM_THREE, logi_led.NUM_ZERO, logi_led.NUM_PERIOD]
neighbor[logi_led.NUM_THREE] = [logi_led.NUM_FIVE, logi_led.NUM_SIX, logi_led.NUM_TWO, logi_led.NUM_ENTER, logi_led.NUM_ZERO, logi_led.NUM_PERIOD]
neighbor[logi_led.NUM_ENTER] = [logi_led.NUM_SIX, logi_led.NUM_PLUS, logi_led.NUM_THREE, logi_led.NUM_PERIOD]

neighbor[logi_led.LEFT_CONTROL] = [logi_led.G_4, logi_led.LEFT_SHIFT, logi_led.G_5, logi_led.LEFT_WINDOWS]
neighbor[logi_led.LEFT_WINDOWS] = [logi_led.LEFT_SHIFT, logi_led.Z, logi_led.LEFT_CONTROL, logi_led.LEFT_ALT, logi_led.G_BADGE]
neighbor[logi_led.LEFT_ALT] = [logi_led.Z, logi_led.X, logi_led.LEFT_WINDOWS, logi_led.G_BADGE]
neighbor[logi_led.SPACE] = [logi_led.V, logi_led.B, logi_led.N]
neighbor[logi_led.RIGHT_ALT] = [logi_led.COMMA, logi_led.PERIOD, logi_led.RIGHT_WINDOWS]
neighbor[logi_led.RIGHT_WINDOWS] = [logi_led.PERIOD, logi_led.FORWARD_SLASH, logi_led.RIGHT_ALT, logi_led.APPLICATION_SELECT]
neighbor[logi_led.APPLICATION_SELECT] = [logi_led.FORWARD_SLASH, logi_led.RIGHT_SHIFT, logi_led.RIGHT_WINDOWS, logi_led.RIGHT_CONTROL]
neighbor[logi_led.RIGHT_CONTROL] = [logi_led.RIGHT_SHIFT, logi_led.APPLICATION_SELECT, logi_led.ARROW_LEFT]
neighbor[logi_led.ARROW_LEFT] = [logi_led.ARROW_UP, logi_led.RIGHT_CONTROL, logi_led.ARROW_DOWN]
neighbor[logi_led.ARROW_DOWN] = [logi_led.ARROW_UP, logi_led.ARROW_LEFT, logi_led.ARROW_RIGHT]
neighbor[logi_led.ARROW_RIGHT] = [logi_led.ARROW_UP, logi_led.NUM_ONE, logi_led.ARROW_DOWN, logi_led.NUM_ZERO]
neighbor[logi_led.NUM_ZERO] = [logi_led.NUM_ONE, logi_led.NUM_TWO, logi_led.NUM_THREE, logi_led.ARROW_RIGHT, logi_led.NUM_PERIOD]
neighbor[logi_led.NUM_PERIOD] = [logi_led.NUM_TWO, logi_led.NUM_THREE, logi_led.NUM_ENTER, logi_led.NUM_ZERO]

neighbor[logi_led.G_1] = [logi_led.G_LOGO, logi_led.ESC, logi_led.TILDE, logi_led.G_2, logi_led.TAB]
neighbor[logi_led.G_2] = [logi_led.G_1, logi_led.TILDE, logi_led.TAB, logi_led.G_3, logi_led.CAPS_LOCK]
neighbor[logi_led.G_3] = [logi_led.G_2, logi_led.TAB, logi_led.CAPS_LOCK, logi_led.G_4]
neighbor[logi_led.G_4] = [logi_led.G_3, logi_led.CAPS_LOCK, logi_led.LEFT_SHIFT, logi_led.G_5, logi_led.LEFT_CONTROL]
neighbor[logi_led.G_5] = [logi_led.G_4, logi_led.LEFT_CONTROL]
neighbor[logi_led.G_6] = [logi_led.G_7, logi_led.ESC, logi_led.F1, logi_led.F2]
neighbor[logi_led.G_7] = [logi_led.G_6, logi_led.G_8, logi_led.F1, logi_led.F2, logi_led.F3]
neighbor[logi_led.G_8] = [logi_led.G_7, logi_led.G_9, logi_led.F2, logi_led.F3, logi_led.F4]
neighbor[logi_led.G_9] = [logi_led.G_8, logi_led.F3, logi_led.F4]
neighbor[logi_led.G_LOGO] = []
neighbor[logi_led.G_BADGE] = []


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

boarder = []
boarder.append(logi_led.G_1)
boarder.append(logi_led.G_2)
boarder.append(logi_led.G_3)
boarder.append(logi_led.G_4)
boarder.append(logi_led.G_5)
boarder.append(logi_led.G_6)
boarder.append(logi_led.G_7)
boarder.append(logi_led.G_8)
boarder.append(logi_led.G_9)
boarder.append(logi_led.G_LOGO)
boarder.append(logi_led.G_BADGE)

boarder.append(logi_led.ESC)
boarder.append(logi_led.F5)
boarder.append(logi_led.F6)
boarder.append(logi_led.F7)
boarder.append(logi_led.F8)
boarder.append(logi_led.F9)
boarder.append(logi_led.F10)
boarder.append(logi_led.F11)
boarder.append(logi_led.F12)
boarder.append(logi_led.PRINT_SCREEN)
boarder.append(logi_led.SCROLL_LOCK)
boarder.append(logi_led.PAUSE_BREAK)

boarder.append(logi_led.NUM_LOCK)
boarder.append(logi_led.NUM_SLASH)
boarder.append(logi_led.NUM_ASTERISK)
boarder.append(logi_led.NUM_MINUS)

boarder.append(logi_led.NUM_PLUS)
boarder.append(logi_led.NUM_ENTER)

boarder.append(logi_led.LEFT_CONTROL)
boarder.append(logi_led.LEFT_WINDOWS)
boarder.append(logi_led.SPACE)
boarder.append(logi_led.RIGHT_ALT)
boarder.append(logi_led.RIGHT_WINDOWS)
boarder.append(logi_led.APPLICATION_SELECT)
boarder.append(logi_led.RIGHT_CONTROL)
boarder.append(logi_led.ARROW_LEFT)
boarder.append(logi_led.ARROW_DOWN)
boarder.append(logi_led.ARROW_RIGHT)
boarder.append(logi_led.NUM_ZERO)
boarder.append(logi_led.NUM_PERIOD)

Rbrightiness = [1.0, 0.95, 0.9, 0.85, 0.8, 0.7, 0.65, 0.6, 0.5, 0.45, 0.4, 0.3, 0.35, 0.3, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0]
Gbrightiness = [1.0, 0.95, 0.9, 0.85, 0.8, 0.7, 0.65, 0.6, 0.5, 0.45, 0.4, 0.3, 0.35, 0.3, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0]
Bbrightiness = [1.0, 0.95, 0.9, 0.85, 0.8, 0.7, 0.65, 0.6, 0.5, 0.45, 0.4, 0.3, 0.35, 0.3, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0]

class touching_effect:
	def __init__(self, pos, red, green, blue, gen = 0):
		self.sta = [list(pos), []]
		self.state = 0
		self.vst = {x:0 for x in pos}
		self.red = red
		self.green = green
		self.blue = blue
		self.gen = gen
		#if pos in boarder:
		#	self.gen = 1
	
	def next(self):
		nstate = 0
		if(self.state == 0):
			nstate = 1
		for tar in self.vst.keys():
			self.vst[tar] = min(self.vst[tar] + 1, 20)
		for tar in self.sta[self.state]:
			for nei in neighbor[tar]:
				if nei not in self.vst.keys():
					self.sta[nstate].append(nei)
					self.vst[nei] = 0
		self.sta[self.state] = []
		self.state = nstate
		self.red = int(self.red * 0.95)
		self.green = int(self.green * 0.95)
		self.blue = int(self.blue * 0.95)
		return self.sta[self.state]

class keyboard_effect:
	
	def __init__(self):
		self.active_effect = []
		"""
		self.active_effect_d1 = []
		self.active_effect_d2 = []
		self.active_effect_d3 = []
		self.active_effect_d4 = []
		self.active_effect_d5 = []
		self.active_effect_d6 = []
		"""
		self.bitmap = [chr(0),chr(0),chr(0),chr(255)]*21*7

	def touching(self, key_name, red = 255, green = 255, blue = 255, gen = 0):
		self.active_effect.append(touching_effect([key_name], int(red*1.0), int(green*1.0), int(blue*1.0), gen))
		"""
		self.active_effect_d1.append(touching_effect([key_name], int(red*0.9), int(green*0.8), int(blue*0.9), gen))
		self.active_effect_d2.append(touching_effect([key_name], int(red*0.5), int(green*0.5), int(blue*0.5), gen))
		self.active_effect_d3.append(touching_effect([key_name], int(red*0.1), int(green*0.1), int(blue*0.1), gen))
		self.active_effect_d4.append(touching_effect([key_name], int(red*0.3), int(green*0.2), int(blue*0.3), gen))
		self.active_effect_d5.append(touching_effect([key_name], int(red*0.6), int(green*0.4), int(blue*0.6), gen))
		self.active_effect_d6.append(touching_effect([key_name], int(red*0.2), int(green*0.1), int(blue*0.2), gen))
		"""
		self.bitmap[keyTObit[key_name]+2] = chr(max(ord(self.bitmap[keyTObit[key_name]+2]), red))
		self.bitmap[keyTObit[key_name]+1] = chr(max(ord(self.bitmap[keyTObit[key_name]+1]), green))
		self.bitmap[keyTObit[key_name]+0] = chr(max(ord(self.bitmap[keyTObit[key_name]+0]), blue))
		self.draw_by_bitmap()

	def next(self):
		for tar_effect in self.active_effect:
			for tar in tar_effect.vst.keys():
				self.bitmap[keyTObit[tar]+2] = chr(0)
				self.bitmap[keyTObit[tar]+1] = chr(0)
				self.bitmap[keyTObit[tar]+0] = chr(0)
			tar_effect.next()
		#self.active_effect[:] = [x for x in self.active_effect if max(x.red, x.green, x.blue) > 40 ]
		"""
		for tar_effect in self.active_effect_d1:
			self.active_effect.append(tar_effect)
		self.active_effect_d1 = self.active_effect_d2
		self.active_effect_d2 = self.active_effect_d3
		self.active_effect_d3 = self.active_effect_d4
		self.active_effect_d4 = self.active_effect_d5
		self.active_effect_d5 = self.active_effect_d6
		self.active_effect_d6 = []
		"""
		for tar_effect in self.active_effect:
			for tar in tar_effect.vst.keys():
				self.bitmap[keyTObit[tar]+2] = chr(max(ord(self.bitmap[keyTObit[tar]+2]), int(tar_effect.red*Rbrightiness[tar_effect.vst[tar]])))
				self.bitmap[keyTObit[tar]+1] = chr(max(ord(self.bitmap[keyTObit[tar]+1]), int(tar_effect.green*Gbrightiness[tar_effect.vst[tar]])))
				self.bitmap[keyTObit[tar]+0] = chr(max(ord(self.bitmap[keyTObit[tar]+0]), int(tar_effect.blue*Bbrightiness[tar_effect.vst[tar]])))
		self.draw_by_bitmap()

	def draw_by_bitmap(self):
		logi_led.logi_led_set_lighting_from_bitmap("".join(self.bitmap))
		for i in range(21*4*6, 21*4*6+11*4,4):
			if ord(self.bitmap[i+3]) != 0:
				logi_led.logi_led_set_lighting_for_key_with_key_name(keyTObit.keys()[keyTObit.values().index(i)],ord(self.bitmap[i+2])*100/255,ord(self.bitmap[i+1])*100/255,ord(self.bitmap[i])*100/255)

def mpause():
	time.sleep(0.05)

KE = keyboard_effect()


while True:
	KE.next()
	KE.touching(random.choice(keyTObit.keys()), random.randint(250,255), 0, 0)
	for i in range(0,15):
		mpause()
		KE.next()
	KE.touching(random.choice(keyTObit.keys()), 0, random.randint(250,255), 0)
	for i in range(0,15):
		mpause()
		KE.next()
	KE.touching(random.choice(keyTObit.keys()), 0, 0, random.randint(250,255))
	for i in range(0,15):
		mpause()
		KE.next()



raw_input( "end" )

logi_led.logi_led_shutdown()
