import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


# LED snippets
##############
# Set all device lighting to red
from logipy import logi_led
import time
import ctypes


val = logi_led.logi_led_init()
print "init = ",val
time.sleep(1) # Give the SDK a second to initialize

#neighbor = {}
neighbor[logiled.ESC] = [logiled.G6, logiled.F1, logiled.ONE, logiled.TILDE, logiled.G1]
neighbor[logiled.F1] = [logiled.G6, logiled.G7, logiled.ESC, logiled.F2, logiled.ONE, logiled.TWO]
neighbor[logiled.F2] = [logiled.G6, logiled.G7, logiled.G8, logiled.F1, logiled.F3, logiled.TWO, logiled.THREE]
neighbor[logiled.F3] = [logiled.G7, logiled.G8, logiled.G9, logiled.F2, logiled.F4, logiled.THREE, logiled.FOUR]
neighbor[logiled.F4] = [logiled.G8, logiled.G9, logiled.F3, logiled.F5, logiled.FOUR, logiled.FIVE]
neighbor[logiled.F5] = [logiled.G9, logiled.F4, logiled.F6, logiled.FIVE, logiled.SIX, logiled.SEVEN]
neighbor[logiled.F6] = [logiled.F5, logiled.F7, logiled.SEVEN, logiled.EIGHT]
neighbor[logiled.F7] = [logiled.F6, logiled.F8, logiled.EIGHT, logiled.NINE]
neighbor[logiled.F8] = [logiled.F7, logiled.F9, logiled.NINE, logiled.ZERO]
neighbor[logiled.F9] = [logiled.F8, logiled.F10, logiled.ZERO, logiled.MINUS, logiled.EQUALS]
neighbor[logiled.F10] = [logiled.F9, logiled.F11, logiled.MINUS, logiled.EQUALS]
neighbor[logiled.F11] = [logiled.F10, logiled.F12, logiled.EQUALS, logiled.BACK_SPACE]
neighbor[logiled.F12] = [logiled.F11, logiled.PRINT_SCREEN, logiled.BACK_SPACE]
neighbor[logiled.PRINT_SCREEN] = [logiled.F12, logiled.SCROLL_LOCK, logiled.INSERT, logiled.HOME]
neighbor[logiled.SCROLL_LOCK] = [logiled.PRINT_SCREEN, logiled.PAUSE_BREAK, logiled.INSERT, logiled.HOME, logiled.PAGE_UP]
neighbor[logiled.PAUSE_BREAK] = [logiled.SCROLL_LOCK, logiled.HOME, logiled.PAGE_UP, logiled.NUM_LOCK]

neighbor[logiled.TILDE] = [logiled.ESC, logiled.G1, logiled.ONE, logiled.G2, logiled.TAB]
neighbor[logiled.ONE] = [logiled.ESC, logiled.F1, logiled.TILDE, logiled.TWO, logiled.TAB, logiled.Q]
neighbor[logiled.TWO] = [logiled.F1, logiled.F2, logiled.ONE, logiled.THREE, logiled.Q, logiled.W]
neighbor[logiled.THREE] = [logiled.F2, logiled.F3, logiled.TWO, logiled.FOUR, logiled.W, logiled.E]
neighbor[logiled.FOUR] = [logiled.F3, logiled.F4, logiled.THREE, logiled.FIVE, logiled.E, logiled.R]
neighbor[logiled.FIVE] = [logiled.F4, logiled.FOUR, logiled.SIX, logiled.R, logiled.T]
neighbor[logiled.SIX] = [logiled.F5, logiled.FIVE, logiled.SEVEN, logiled.T, logiled.Y]
neighbor[logiled.SEVEN] = [logiled.F5, logiled.F6, logiled.SIX, logiled.SIGHT, logiled.Y, logiled.U]
neighbor[logiled.EIGHT] = [logiled.F6, logiled.F7, logiled.SEVEN, logiled.NINE, logiled.U, logiled.I]
neighbor[logiled.NINE] = [logiled.F7, logiled.F8, logiled.EIGHT, logiled.ZERO, logiled.I, logiled.O]
neighbor[logiled.ZERO] = [logiled.F8, logiled.F9, logiled.NINE, logiled.MINUS, logiled.O, logiled.P]
neighbor[logiled.MINUS] = [logiled.F9, logiled.F10, logiled.ZERO, logiled.EQUALS, logiled.P, logiled.OPEN_BRACKET]
neighbor[logiled.EQUALS] = [logiled.F10, logiled.F11, logiled.MINUS, logiled.BACK_SPACE, logiled.OPEN_BRACKET, logiled.CLOSE_BRACKET]
neighbor[logiled.BACK_SPACE] = [logiled.F11, logiled.F12, logiled.EQUALS, logiled.INSERT, logiled.CLOSE_BRACKET, logiled.BACKSLASH]
neighbor[logiled.INSERT] = [logiled.F12, logiled.PRINT_SCREEN, logiled.SCROLL_LOCK, logiled.BACK_SPACE, logiled.HOME, logiled.BACKSLASH, logiled.KEYBOARD_DELETE, logiled.END]
neighbor[logiled.HOME] = [logiled.PRINT_SCREEN, logiled.SCROLL_LOCK, logiled.PAUSE_BREAK, logiled.INSERT, logiled.PAGE_UP, logiled.KEYBOARD_DELETE, logiled.END, logiled.PAGE_DOWN]
neighbor[logiled.PAGE_UP] = [logiled.SCROLL_LOCK, logiled.PAUSE_BREAK, logiled.HOME, logiled.NUM_LOCK, logiled.END, logiled.PAGE_DOWN]
neighbor[logiled.NUM_LOCK] = [logiled.PAUSE_BREAK, logiled.PAGE_UP, logiled.NUM_SLASH, logiled.PAGE_DOWN, logiled.NUM_SEVEN, logiled.NUM_EIGHT]
neighbor[logiled.NUM_SLASH] = [logiled.NUM_LOCK, logiled.NUM_ASTERISK, logiled.NUM_SEVEN, logiled.NUM_EIGHT, logiled.NUM_NINE]
neighbor[logiled.NUM_ASTERISK] = [logiled.NUM_SLASH, logiled.NUM_MINUS, logiled.NUM_EIGHT, logiled.NUM_NINE, logiled.NUM_PLUS]
neighbor[logiled.NUM_MINUS] = [logiled.NUM_ASTERISK, logiled.NUM_NINE, logiled.NUM_PLUS]

neighbor[logiled.TAB] = [logiled.G1, logiled.TILDE, logiled.ONE, logiled.G2, logiled.Q, logiled.G3, logiled.CAPS_LOCK]
neighbor[logiled.Q] = [logiled.ONE, logiled.TWO, logiled.TAB, logiled.W, logiled.CAPS_LOCK, logiled.A]
neighbor[logiled.W] = [logiled.TWO, logiled.THREE, logiled.Q, logiled.E, logiled.A, logiled.S]
neighbor[logiled.E] = [logiled.THREE, logiled.FOUR, logiled.W, logiled.R, logiled.S, logiled.D]
neighbor[logiled.R] = [logiled.FOUR, logiled.FIVE, logiled.E, logiled.T, logiled.D, logiled.F]
neighbor[logiled.T] = [logiled.FIVE, logiled.SIX, logiled.R, logiled.Y, logiled.F, logiled.G]
neighbor[logiled.Y] = [logiled.SIX, logiled.SEVEN, logiled.T, logiled.U, logiled.G, logiled.H]
neighbor[logiled.U] = [logiled.SEVEN, logiled.EIGHT, logiled.Y, logiled.I, logiled.H, logiled.J]
neighbor[logiled.I] = [logiled.EIGHT, logiled.NINE, logiled.U, logiled.O, logiled.J, logiled.K]
neighbor[logiled.O] = [logiled.NINE, logiled.ZERO, logiled.I, logiled.P, logiled.K, logiled.L]
neighbor[logiled.P] = [logiled.ZERO, logiled.MINUS, logiled.O, logiled.OPEN_BRACKET, logiled.L, logiled.SEMICOLON]
neighbor[logiled.OPEN_BRACKET] = [logiled.MINUS, logiled.EQUALS, logiled.P, logiled.CLOSE_BRACKET, logiled.SEMICOLON, logiled.APOSTROPHE]
neighbor[logiled.CLOSE_BRACKET] = [logiled.EQUALS, logiled.BACK_SPACE, logiled.OPEN_BRACKET, logiled.BACKSLASH, logiled.APOSTROPHE, logiled.ENTER]
neighbor[logiled.BACKSLASH] = [logiled.BACK_SPACE, logiled.INSERT, logiled.CLOSE_BRACKET, logiled.KEYBOARD_DELETE, logiled.ENTER]
neighbor[logiled.KEYBOARD_DELETE] = [logiled.INSERT, logiled.HOME, logiled.BACKSLASH, logiled.END]
neighbor[logiled.END] = [logiled.INSERT, logiled.HOME, logiled.PAGE_UP, logiled.KEYBOARD_DELETE, logiled.PAGE_DOWN]
neighbor[logiled.PAGE_DOWN] = [logiled.HOME, logiled.PAGE_UP, logiled.NUM_LOCK, logiled.END, logiled.NUM_SEVEN, logiled.NUM_FOUR]
neighbor[logiled.NUM_SEVEN] = [logiled.PAGE_UP, logiled.NUM_LOCK, logiled.NUM_SLASH, logiled.PAGE_DOWN, logiled.NUM_EIGHT, logiled.NUM_FOUR, logiled.NUM_FIVE]
neighbor[logiled.NUM_EIGHT] = [logiled.NUM_LOCK, logiled.NUM_SLASH, logiled.NUM_ASTERISK, logiled.NUM_SEVEN, logiled.NUM_NINE, logiled.NUM_FOUR, logiled.NUM_FIVE, logiled.NUM_SIX]
neighbor[logiled.NUM_NINE] = [logiled.NUM_SLASH, logiled.NUM_ASTERISK, logiled.NUM_MINUS, logiled.NUM_EIGHT, logiled.NUM_PLUS, logiled.NUM_FIVE, logiled.NUM_SIX]
neighbor[logiled.NUM_PLUS] = [logiled.NUM_ASTERISK, logiled.NUM_MINUS, logiled.NUM_NINE, logiled.NUM_SIX, logiled.NUM_THREE, logiled.NUM_ENTER]

neighbor[logiled.CAPS_LOCK] = [logiled.G2, logiled.TAB, logiled.Q, logiled.G3, logiled.A, logiled.G4, logiled.LEFT_SHIFT]
neighbor[logiled.A] = [logiled.Q, logiled.W, logiled.CAPS_LOCK, logiled.S, logiled.LEFT_SHIFT, logiled.Z]
neighbor[logiled.S] = [logiled.W, logiled.E, logiled.A, logiled.D, logiled.Z, logiled.X]
neighbor[logiled.D] = [logiled.E, logiled.R, logiled.S, logiled.F, logiled.X, logiled.C]
neighbor[logiled.F] = [logiled.R, logiled.T, logiled.D, logiled.G, logiled.C, logiled.V]
neighbor[logiled.G] = [logiled.T, logiled.Y, logiled.F, logiled.H, logiled.V, logiled.B]
neighbor[logiled.H] = [logiled.Y, logiled.U, logiled.G, logiled.J, logiled.B, logiled.N]
neighbor[logiled.J] = [logiled.U, logiled.I, logiled.H, logiled.K, logiled.N, logiled.M]
neighbor[logiled.K] = [logiled.I, logiled.O, logiled.J, logiled.L, logiled.M, logiled.COMMA]
neighbor[logiled.L] = [logiled.O, logiled.P, logiled.K, logiled.SEMICOLON, logiled.COMMA, logiled.PERIOD]
neighbor[logiled.SEMICOLON] = [logiled.P, logiled.OPEN_BRACKET, logiled.L, logiled.APOSTROPHE, logiled.PERIOD, logiled.FORWARD_SLASH]
neighbor[logiled.APOSTROPHE] = [logiled.OPEN_BRACKET, logiled.CLOSE_BRACKET, logiled.SEMICOLON, logiled.ENTER, logiled.FORWARD_SLASH, logiled.RIGHT_SHIFT]
neighbor[logiled.ENTER] = [logiled.CLOSE_BRACKET, logiled.BACKSLASH, logiled.APOSTROPHE, logiled.RIGHT_SHIFT]
neighbor[logiled.NUM_FOUR] = [logiled.PAGE_DOWN, logiled.NUM_SEVEN, logiled.NUM_EIGHT, logiled.NUM_FIVE, logiled.NUM_ONE, logiled.NUM_TWO]
neighbor[logiled.NUM_FIVE] = [logiled.NUM_SEVEN, logiled.NUM_EIGHT, logiled.NUM_NINE, logiled.NUM_FOUR, logiled.NUM_SIX, logiled.NUM_ONE, logiled.NUM_TWO, logiled.THREE]
neighbor[logiled.NUM_SIX] = [logiled.NUM_EIGHT, logiled.NUM_NINE, logiled.NUM_PLUS, logiled.NUM_FIVE, logiled.NUM_TWO, logiled.THREE, logiled.NUM_ENTER]

neighbor[logiled.LEFT_SHIFT] = [logiled.G3, logiled.CAPS_LOCK, logiled.A, logiled.G4, logiled.Z, logiled.LEFT_CONTROL, logiled.LEFT_WINDOWS]
neighbor[logiled.Z] = [logiled.A, logiled.S, logiled.LEFT_SHIFT, logiled.X, logiled.LEFT_WINDOWS, logiled.LEFT_ALT]
neighbor[logiled.X] = [logiled.S, logiled.D, logiled.Z, logiled.C, logiled.LEFT_ALT]
neighbor[logiled.C] = [logiled.D, logiled.F, logiled.X, logiled.V]
neighbor[logiled.V] = [logiled.F, logiled.G, logiled.C, logiled.B]
neighbor[logiled.B] = [logiled.G, logiled.H, logiled.V, logiled.N, logiled.SPACE]
neighbor[logiled.N] = [logiled.H, logiled.J, logiled.B, logiled.M, logiled.SPACE]
neighbor[logiled.M] = [logiled.J, logiled.K, logiled.N, logiled.COMMA]
neighbor[logiled.COMMA] = [logiled.K, logiled.L, logiled.M, logiled.PERIOD, logiled.RIGHT_ALT]
neighbor[logiled.PERIOD] = [logiled.L, logiled.SEMICOLON, logiled.COMMA, logiled.FORWARD_SLASH, logiled.RIGHT_ALT, logiled.RIGHT_WINDOWS]
neighbor[logiled.FORWARD_SLASH] = [logiled.SEMICOLON, logiled.APOSTROPHE, logiled.PERIOD, logiled.RIGHT_SHIFT, logiled.RIGHT_WINDOWS, logiled.APPLICATION_SELECT]
neighbor[logiled.RIGHT_SHIFT] = [logiled.APOSTROPHE, logiled.ENTER, logiled.FORWARD_SLASH, logiled.APPLICATION_SELECT, logiled.RIGHT_CONTROL]
neighbor[logiled.ARROW_UP] = [logiled.ARROW_LEFT, logiled.ARROW_DOWN, logiled.ARROW_RIGHT]
neighbor[logiled.NUM_ONE] = [logiled.NUM_FOUR, logiled.NUM_FIVE, logiled.NUM_TWO, logiled.ARROW_RIGHT, logiled.NUM_ZERO]
neighbor[logiled.NUM_TWO] = [logiled.NUM_FOUR, logiled.NUM_FIVE, logiled.SIX, logiled.NUM_ONE, logiled.NUM_THREE, logiled.NUM_ZERO, logiled.NUM_PERIOD]
neighbor[logiled.NUM_THREE] = [logiled.NUM_FIVE, logiled.SIX, logiled.NUM_TWO, logiled.NUM_ENTER, logiled.NUM_ZERO, logiled.NUM_PERIOD]
neighbor[logiled.NUM_ENTER] = [logiled.SIX, logiled.NUM_PLUS, logiled.NUM_THREE, logiled.NUM_PERIOD]

neighbor[logiled.LEFT_CONTROL] = [logiled.G4, logiled.LEFT_SHIFT, logiled.G5, logiled.LEFT_WINDOWS]
neighbor[logiled.LEFT_WINDOWS] = [logiled.LEFT_SHIFT, logiled.Z, logiled.LEFT_CONTROL, logiled.LEFT_ALT]
neighbor[logiled.LEFT_ALT] = [logiled.Z, logiled.X, logiled.LEFT_WINDOWS]
neighbor[logiled.SPACE] = [logiled.X, logiled.C, logiled.V, logiled.B, logiled.N, logiled.M, logiled.COMMA, logiled.LEFT_ALT, logiled.RIGHT_ALT]
neighbor[logiled.RIGHT_ALT] = [logiled.COMMA, logiled.PERIOD, logiled.RIGHT_WINDOWS]
neighbor[logiled.RIGHT_WINDOWS] = [logiled.PERIOD, logiled.FORWARD_SLASH, logiled.RIGHT_ALT, logiled.APPLICATION_SELECT]
neighbor[logiled.APPLICATION_SELECT] = [logiled.FORWARD_SLASH, logiled.RIGHT_SHIFT, logiled.RIGHT_WINDOWS, logiled.RIGHT_CONTROL]
neighbor[logiled.RIGHT_CONTROL] = [logiled.RIGHT_SHIFT, logiled.APPLICATION_SELECT, logiled.ARROW_LEFT]
neighbor[logiled.ARROW_LEFT] = [logiled.ARROW_UP, logiled.RIGHT_CONTROL, logiled.ARROW_DOWN]
neighbor[logiled.ARROW_DOWN] = [logiled.ARROW_UP, logiled.ARROW_LEFT, logiled.ARROW_RIGHT]
neighbor[logiled.ARROW_RIGHT] = [logiled.ARROW_UP, logiled.NUM_ONE, logiled.ARROW_DOWN, logiled.NUM_ZERO]
neighbor[logiled.NUM_ZERO] = [logiled.NUM_ONE, logiled.NUM_TWO, logiled.NUM_THREE, logiled.ARROW_RIGHT, logiled.NUM_PERIOD]
neighbor[logiled.NUM_PERIOD] = [logiled.NUM_TWO, logiled.NUM_THREE, logiled.NUM_ENTER, logiled.NUM_ZERO]

neighbor[logiled.G1] = [logiled.ESC, logiled.TILDE, logiled.G2, logiled.TAB]
neighbor[logiled.G2] = [logiled.G1, logiled.TILDE, logiled.TAB, logiled.G3, logiled.CAPS_LOCK]
neighbor[logiled.G3] = [logiled.G2, logiled.TAB, logiled.CAPS_LOCK, logiled.G4]
neighbor[logiled.G4] = [logiled.G3, logiled.CAPS_LOCK, logiled.LEFT_SHIFT, logiled.G5, logiled.LEFT_CONTROL]
neighbor[logiled.G5] = [logiled.G4, logiled.LEFT_CONTROL]
neighbor[logiled.G6] = [logiled.G7, logiled.ESC, logiled.F1, logiled.F2]
neighbor[logiled.G7] = [logiled.G6, logiled.G8, logiled.F1, logiled.F2, logiled.F3]
neighbor[logiled.G8] = [logiled.G7, logiled.G9, logiled.F2, logiled.F3, logiled.F4]
neighbor[logiled.G9] = [logiled.G8, logiled.F3, logiled.F4]





raw_input( "end" )

