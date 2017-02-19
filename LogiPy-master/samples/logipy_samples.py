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
notification.balloon_tip( "hey" , "gay" )


print ('Setting all device lighting to red...')
val = logi_led.logi_led_init()
print val
time.sleep(1) # Give the SDK a second to initialize
val = logi_led.logi_led_set_lighting(100, 0 , 0)
raw_input( "wait" )
# If you prefer the c/c++ style you can use the DLL directly
print ('Setting all device lighting to green...')
logi_led.led_dll.LogiLedSetLighting(ctypes.c_int(0), ctypes.c_int(100), ctypes.c_int(0))
raw_input('Press enter to shutdown SDK...')
logi_led.led_dll.LogiLedShutdown()


# Arx snippets
##############

# Show a simple applet with the default callback
# note: will not work if a callback has already been defined by the process
from logipy import logi_arx
import time
print ('Setting up a simple applet...')

# Show a simple applet with a custom callback
from logipy import logi_arx
import time
import ctypes

print 'Setting up a simple applet with custom callback...'
index = """
         <html>
    <head>
        <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <link rel="stylesheet" type="text/css" href="style.css">
        <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<script
  src="https://code.jquery.com/jquery-3.1.1.min.js"
  integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
  crossorigin="anonymous"></script>    
</head>
    <body>
    <div id="mainContent" class="container" style="margin-top:30px;">
        <div class="row">
            <div class="col-xs-3" >
                <img class="img-responsive img-circle" src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQjMQSVoXBDjYUpZm9a-HLx0IiKIr6wuujnCcNU8Ou006uihh3n9g" >
            </div>
            <div class="col-xs-9">
                <blockquote>
                  <p>
                  Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
                  </p>
                </blockquote>
            </div>
        </div>
         <div class="row">
            <div class="col-xs-3" >
                <img class="img-responsive img-circle" src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQjMQSVoXBDjYUpZm9a-HLx0IiKIr6wuujnCcNU8Ou006uihh3n9g" >
            </div>
            <div class="col-xs-9">
                <blockquote>
                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
                </blockquote>
            </div>
        </div>
    </div>
    </body>

    </html>
    """
def custom_callback(event_type, event_value, event_arg, context):
    if event_arg and event_arg == 'splash-icon':
        print '\nNo wonder Logitech is called Logicool in Japan! They are so cool!'

logi_arx.logi_arx_init('com.logitech.gaming.logipy', 'LogiPy', custom_callback)
time.sleep(1)
logi_arx.logi_arx_add_utf8_string_as(index, 'index.html', 'text/html')
logi_arx.logi_arx_add_utf8_string_as("GOOd", 'good.html' , 'text/html')



logi_arx.logi_arx_set_index('index.html')
raw_input('Press enter to shutdown SDK...')
logi_arx.logi_arx_shutdown()