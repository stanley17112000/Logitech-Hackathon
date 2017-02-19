import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# LED snippets
##############
from notification import notification, notificationEX
# Set all device lighting to red
from logipy import logi_led
from logipy import logi_gkey
import time
import ctypes

print logi_gkey.logi_gkey_init()
print logi_led.logi_led_init()
notification.balloon_tip( "hey" , "gay" )
time.sleep(1) # Give the SDK a second to initialize
raw_input('Press enter to shutdown SDK...')
logi_led.led_dll.LogiLedShutdown()

# Arx snippets
##############

# Show a simple applet with the default callback
# note: will not work if a callback has already been defined by the process
from logipy import logi_arx
import time
print 'Setting up a simple applet...'

# Show a simple applet with a custom callback
from logipy import logi_arx
import time
import ctypes

print 'Setting up a simple applet with custom callback...'
f = open('..\\..\\ARX Layout\\index.html', 'r')
index = f.read()

def custom_callback(event_type, event_value, event_arg, context):
    if event_arg and event_arg == 'splash-icon':
        print '\nNo wonder Logitech is called Logicool in Japan! They are so cool!'

logi_arx.logi_arx_init('com.logitech.gaming.logipy', 'LogiPy', custom_callback)
time.sleep(1)
logi_arx.logi_arx_add_utf8_string_as(index, 'index.html', 'text/html')
logi_arx.logi_arx_set_index('index.html')

raw_input('Press enter to shutdown SDK...')
logi_arx.logi_arx_shutdown()