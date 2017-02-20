# coding = UTF-8
# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from notification import notification, notificationEX
from logipy import logi_led, logi_gkey
import time
import ctypes
import pythoncom
import pyHook
import threading
import fbchat
import random
import json
from logipy import logi_arx
import logging
import html
import cgi
from lights import light
import touching_effect
logging.getLogger("fbchat").setLevel(logging.WARNING)
fb_line = light()
KE = touching_effect.keyboard_effect()
te_stop = threading.Event()
threading.Thread( target = touching_effect.graph_effect, args = (KE, te_stop)).start()

def switch_led():
    te_stop.set()
    fb_line.facebook_led(100, 0.1)
    te_stop.clear()

#G2/M3

class EchoBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)
        self.message_list = []
        self.icon_index = 0
        self.user_index = []   #[author_id:index]
        self.pivot = 0 #pointer to the friend of the arx page

    def on_message(self, mid, author_id, author_name, message, metadata):
        
        global contact,name_list
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read
        if str(author_id) != '100015293506097':
            threading.Thread( target = switch_led, args = () ).start()
            #fb_line.facebook_led(100, 0.1)
            print("%s said: %s"%(author_id, message))
            #update_json(message)
            if author_id not in contact.values():  #initialize the new sender
                num = random.randint(-1,len(name_list)-1) #random name for new sender
                name = name_list[num]
                contact[name] = author_id #sender side  ex:['John':'123123123213']
                name_list.remove(name)
                self.user_index.append(author_id)
                #the index of message_list is the number of the user 
                self.message_list.append({
                    'name':name,
                    'msg':"",
                    'icon':icon[self.icon_index % len(icon)],
                    'author_id':author_id
                })
                self.icon_index += 1
            index = self.user_index.index(author_id)
            self.message_list[index]['msg'] += message+'\n'  # append the new message from the sender
            self.display_message_to_arx()

    #------Move the pivot-----    
    def change_pivot(self,direction):
        #direction : 1 or -1
        self.pivot += direction
        self.pivot %= len(self.message_list)
        if direction is 1:
          update_json({'action':'right'})
        else:
          update_json({'action':'left'})

    #------Send the message user type to FB friend----
    def send_message_to_user(self,index,message):
        if len( self.message_list ) <= index:
            return
        author_id = self.message_list[index]['author_id']
        #message is from GKEY
        self.send(author_id,message)

    #------Ask arx to    
    def send_message_to_arx(self,message):
        update_json({'action':'send','msg':message})

    #------Ask arx to display the FB message
    def display_message_to_arx(self):
        
        pkg = {
            'pivot':self.pivot,
            'action':'display',
            'data': self.message_list
        }
        update_json(pkg)

    #------Update the message user type to arx dynamically----
    def type_message_to_arx(self,messgae_user_type):
        string_from_GKEY = messgae_user_type  #a->ab->abc->abcd->........
        pkg = {
            'action':'type',
            'usertype':string_from_GKEY
        }
        update_json(pkg)
        

flag = 0
#------Handke the GKEY,m1~m3------------------
def gkey_callback(gkeyCode , gkeyOrButtonString,context):
  global  now_mkey , now_gkey , is_key_pressed,state,mouse_counter,type_msg,flag,gkey_onkeyboard,canned_mesage,contact
  print '\n[gKey] default_callback called with: gkeyCode = {gkeyCode}, gkeyOrButtonString = {gkeyOrButtonString}, context = {context}'.format(
  gkeyCode = gkeyCode, gkeyOrButtonString = gkeyOrButtonString, context = context)
  print flag
  flag+=1

  #-------Press the GKEY on the mouse------
  if gkeyOrButtonString == 'Mouse Btn 6':
    mouse_counter += 1
    #------Enter typing mode-------
    if mouse_counter % 4 == 2:
      state = 1
    #------No typing mode--------
    else:
      state = 0
      #--------Send the message user type to the arx and FB friend
      if type_msg != '' and mouse_counter%4==3:
        print '====================',bot.message_list
        print 'u type the sentence:',type_msg
        #bot.send_message_to_arx()
        print 'message_list:',bot.message_list
        bot.send_message_to_user(bot.pivot,type_msg)
        bot.send_message_to_arx(type_msg)
        type_msg = ''
        name = bot.message_list[bot.pivot]['name']
        bot.user_index.remove(contact[name])
        del contact[name]
        bot.message_list.remove(bot.message_list[bot.pivot])
        print '********************',bot.message_list
        time.sleep(2)
        bot.display_message_to_arx()
  #-------Press the other GKEY (and detect which m key is pressed in m1 ~ m3)----
  else:
    now_gkey = int(gkeyOrButtonString[1])
    now_mkey = int(gkeyOrButtonString[4])
    gkey_onkeyboard[now_gkey]+=1
    gkey_onkeyboard[now_gkey]%=4
    #press certain gkey 
    if gkey_onkeyboard[now_gkey] % 4 == 2:
      gkey_onkeyboard[now_gkey] = 0
      if now_mkey == 3:    #The canned message mode
        message = canned_mesage[now_gkey]
        bot.send_message_to_user(bot.pivot,message)
        bot.send_message_to_arx(message)
      elif now_mkey == 2:  #The watching mode
        #odd for right, even for leftd
        if now_gkey % 2 == 1:
          direction = 1
        else:
          direction = -1
        bot.change_pivot(direction)

def listen_on_keyboard():
  global state
  hm = pyHook.HookManager()
  hm.KeyDown = onKeyboardEvent
  hm.HookKeyboard()
  while 1:
    if state == 1:
      pythoncom.PumpWaitingMessages()

def mpause():
	time.sleep(0.04)

def onKeyboardEvent(event):
  global type_msg
  print "EEEEEEE"
  if event.KeyID == 8: #backspace
    type_msg = type_msg[:-1]
  else:
    type_msg += chr(event.Ascii)
  ch = chr(event.Ascii)
  if ch == 'q':
      KE.touching(logi_led.Q, 255, 0, 0)
  elif ch == 'w':
      KE.touching(logi_led.W, 255, 0, 0)
  elif ch == 'e':
      KE.touching(logi_led.E, 255, 0, 0)
  elif ch == 'r':
      KE.touching(logi_led.R, 255, 0, 0)
  elif ch == 't':
      KE.touching(logi_led.T, 255, 0, 0)
  elif ch == 'y':
      KE.touching(logi_led.Y, 255, 0, 0)
  elif ch == 'u':
      KE.touching(logi_led.U, 255, 0, 0)
  elif ch == 'i':
      KE.touching(logi_led.I, 255, 0, 0)
  elif ch == 'o':
      KE.touching(logi_led.O, 255, 0, 0)
  elif ch == 'p':
      KE.touching(logi_led.P, 255, 0, 0)
  elif ch == 'a':
      KE.touching(logi_led.A, 255, 0, 0)
  elif ch == 's':
      KE.touching(logi_led.S, 255, 0, 0)
  elif ch == 'd':
      KE.touching(logi_led.D, 255, 0, 0)
  elif ch == 'f':
      KE.touching(logi_led.F, 255, 0, 0)
  elif ch == 'g':
      KE.touching(logi_led.G, 255, 0, 0)
  elif ch == 'h':
      KE.touching(logi_led.H, 255, 0, 0)
  elif ch == 'j':
      KE.touching(logi_led.J, 255, 0, 0)
  elif ch == 'k':
      KE.touching(logi_led.K, 255, 0, 0)
  elif ch == 'l':
      KE.touching(logi_led.L, 255, 0, 0)
  elif ch == 'z':
      KE.touching(logi_led.Z, 255, 0, 0)
  elif ch == 'x':
      KE.touching(logi_led.X, 255, 0, 0)
  elif ch == 'c':
      KE.touching(logi_led.C, 255, 0, 0)
  elif ch == 'v':
      KE.touching(logi_led.V, 255, 0, 0)
  elif ch == 'b':
      KE.touching(logi_led.B, 255, 0, 0)
  elif ch == 'n':
      KE.touching(logi_led.N, 255, 0, 0)
  elif ch == 'm':
      KE.touching(logi_led.M, 255, 0, 0)
      

  bot.type_message_to_arx(type_msg)
  print 'u type',chr(event.Ascii)
  return True

json_pool = []

def update_json(diction):
    print '====================================='
    s = json.dumps( diction )

   
    s = cgi.escape(s, quote=True)
    l = len( s ) / 10
    for i in range( 10 ):
        mid = 'message' + str(i) 
        if i == 9:
            targetStr = s[l*i:]
        else:
            targetStr = s[l*i:l*(i+1)]

        print mid, '------' ,  targetStr
       

        logi_arx.logi_arx_set_tag_property_by_id( mid , 'value' , targetStr )

    

 

"""
0: init
1: mouse (typing)
2: m1 (nothing)
3: m2 (canned message)
 """
state = 0 

#------GKEY and m1~m3-------
now_mkey = 0
now_gkey = 0
is_key_pressed = False

#---------record the click of the GKEY on the mouse and the keyboard------
mouse_counter = 0
gkey_onkeyboard = [0]*10

#--------message user have typed---------
type_msg = ''

#---------record name and author_id   ex:{'John':'213212321'}
contact = {}

#---------virtual friend initialization
name_list = ['Andy','Henry','John','Logi','NCTU','NTHU']
icon = [
    'https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697057-facebook-512.png',
    'https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697029-twitter-128.png',
    'https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697037-youtube-128.png',
    'https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697034-windows-visual-studio-128.png',
    'https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697067-instagram-128.png'
]

#----canned message-----
canned_mesage=[
  '',
  'I\'m playing game and will reply you later~',
  'I am doing homework, don\'t bother me!',
  'Fu*k you man',
  'That\'s a good idea.',
  'I\'m watching movies, sry.',
  'Yes!',
  'No',
  'That sounds bad!'
]


#------listen on the keyboard-------
threading.Thread(target = listen_on_keyboard, args = ()).start()

#------initialize the GKEY SDK---------
print 'gkey init ..' , logi_gkey.logi_gkey_init(gkey_callback)

logi_arx.logi_arx_init('com.logitech.gaming.logipy', 'LogiPy')
time.sleep(1)
f = open('..\\ARX Layout\\index.html', 'r')
index = f.read()
logi_arx.logi_arx_add_utf8_string_as(index, 'index.html', 'text/html')
logi_arx.logi_arx_set_index( 'index.html' )


#----------FB listener-------------du
bot = EchoBot("stanley17112000.001@gmail.com", "nopassword123")
bot.listen()


time.sleep(100)

