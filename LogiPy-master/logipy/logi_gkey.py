"""
logi_g_key.py : Defines the exported functions for the API

Logitech Gaming G Key Control SDK

Author: Stanley Hong
Email: stanley17112000@gmail.com
"""

import ctypes
import os
import platform

# DLL Definitions
#

LOGITECH_MAX_MOUSE_BUTTONS = 20
LOGITECH_MAX_GKEYS = 29
LOGITECH_MAX_M_STATES = 3

class GkeyCode(ctypes.LittleEndianStructure):
    _field_ = [
        ('keyIdx' , ctypes.c_uint , 8),
        ('keyDown' , ctypes.c_uint , 1),
        ('mState' , ctypes.c_uint , 2),
        ('mouse' , ctypes.c_uint , 1),
        ('reserved1' , ctypes.c_uint , 4 ),
        ('reserved2' , ctypes.c_uint , 16)
    ]



CALLBACK_DEFINITION = ctypes.CFUNCTYPE(None, ctypes.POINTER(GkeyCode) ,  ctypes.c_wchar_p , ctypes.c_void_p)



class logiGkeyCBContext( ctypes.Structure ):
    _fields_ = [
        ('gkeyCallBack' , CALLBACK_DEFINITION),
        ('gkeyContext' , ctypes.c_void_p)
    ]

def callback_wrapper(gkeyCode , gkeyOrButtonString,context):
    on_callback(gkeyCode , gkeyOrButtonString,context)

def default_callback(gkeyCode , gkeyOrButtonString,context):
     print '\n[gKey] default_callback called with: gkeyCode = {gkeyCode}, gkeyOrButtonString = {gkeyOrButtonString}, context = {context}'.format(
     gkeyCode = gkeyCode, gkeyOrButtonString = gkeyOrButtonString, context = context)

# Required Globals
#
class SDKNotFoundException:
    pass

def load_dll(path_dll = None):
  
    if not path_dll:
        bitness = 'x86' if platform.architecture()[0] == '32bit' else 'x64'
        subpath_dll = r'/Logitech Gaming Software/SDK/G-key/{}/LogitechGkey.dll'.format(bitness)
        subpath_lgs = os.environ['ProgramW6432'] if os.environ['ProgramW6432'] else os.environ['ProgramFiles']
        path_dll = subpath_lgs + subpath_dll
    if os.path.exists(path_dll):
        return ctypes.cdll.LoadLibrary(path_dll)
    else:
        raise SDKNotFoundException('The SDK DLL was not found.')

try:
    gkey_dll = load_dll()
except SDKNotFoundException as exception_sdk:
    gkey_dll = None
on_callback = None

def logi_gkey_init( py_callback_function = None):
    """ initializes the applet on the app with the given friendly_name. """
    if gkey_dll:
        global on_callback
        global callback_ref
        on_callback   = py_callback_function if py_callback_function else default_callback
        callback_ref  = ctypes.byref(CALLBACK_DEFINITION(callback_wrapper))
        return bool(gkey_dll.LogiGkeyInit(callback_ref))
    else:
        return False

def logi_gkey_init_without_callback():
    if gkey_dll:
        return bool(gkey_dll.LogiGkeyInitWithoutCallback())
    else:
        return False

def logi_gkey_init_without_context( gkey_call_back ):
    if gkey_dll:
        gkey_call_back = CALLBACK_DEFINITION( gkey_call_back )
        return bool(gkey_dll.LogiGkeyInitWithoutContext( gkey_call_back ))
    else:
        return False


def logi_gkey_is_mouse_button_pressed( button_number ):
    if gkey_dll:
         button_number = ctypes.c_int( button_number )
         return bool(gkey_dll.LogiGkeyIsMouseButtonPressed( button_number ))
    else:
         return False

def logi_gkey_get_mouse_button_string( button_number ):
    if gkey_dll:
        button_number = ctypes.c_int( button_number )
        return str( gkey_dll.LogiGkeyGetMouseButtonString( button_number ) )
    else:
        return None

def logi_gkey_is_keyboard_key_pressed( gkey_number , mode_number ):
    if gkey_dll:
        gkey_number = ctypes.c_int( gkey_number )
        mode_number = ctypes.c_int( mode_number )
        return bool( gkey_dll.LogiGkeyIsKeyboardGkeyPressed( gkey_number , mode_number ) )
    else:
        return False

def logi_gkey_is_keyboard_key_pressed( gkey_number , mode_number ):
    if gkey_dll:
        gkey_number = ctypes.c_int( gkey_number )
        mode_number = ctypes.c_int( mode_number )
        return str( gkey_dll.LogiGkeyGetKeyboardGkeyString( gkey_number , mode_number ) )
    else:
        return None

def logi_gkey_shutdown():
    if gkey_dll:
        gkey_dll.LogiGkeyShutdown()
    