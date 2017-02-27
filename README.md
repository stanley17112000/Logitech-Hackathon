# Logitech-Hackathon

This is a Python2.7 Project wroten in Logitech Hackday 2017.

It demonstrates the connection between Logitech G-series gaming keyboard and Android/IOS phones. One can easily reply message ( FB/Line ) when doing other tasks( Ex. Full screen online game ). 

When message is received( Ex. FB ), you will be notified by keyboard lights. 
Switch different sender's messages by clicking G6/G7. 
Fast reply with can message by clicking G1~G5.
Click M2 to start typing mode, reply message with keyboard typing.


* A special lighting effect included

# Structure

ARX Layout
-----------------------------------
        - index.html : the layout of client side, it's based on html

LogiPy-master
-----------------------------------
        - server.py : Main server code, connecting with FB's api, receiving keyboard events and deliever views to client
        - touching_effect.py : A special lighting effect
        - logipy/logi_gkey.py : A new added python wrapper for g_key sdk
        - lights.py : lighting effect when message comes
