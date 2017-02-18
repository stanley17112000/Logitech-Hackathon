import fbchat
client = fbchat.Client("YOUR_ID", "YOUR_PASSWORD")



class Friend:
    def __init__ ( self , 5 ):


def sendMessage( msg ):
    friends = client.getUsers("FRIEND'S NAME")  # return a list of names
    friend = friends[0]
    sent = client.send(friend.uid, "Your Message")
    if sent:
        print("Message sent successfully!")
    # IMAGES
    client.sendLocalImage(friend.uid,message='<message text>',image='<path/to/image/file>') # send local image
    imgurl = "http://i.imgur.com/LDQ2ITV.jpg"
    client.sendRemoteImage(friend.uid,message='<message text>', image=imgurl) # send image from image url