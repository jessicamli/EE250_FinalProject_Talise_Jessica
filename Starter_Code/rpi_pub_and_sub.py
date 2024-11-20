"""EE 250L Lab 04 Starter Code

Group Members: Talise Baker-Matsuoka and Jessica Li
GitHub Link: https://github.com/usc-ee250-fall2024/mqtt-talise-and-jessica.git

Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time
import sys
import grovepi
from grove_rgb_lcd import *
import threading

# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

# Connect the Grove LED to digital port D3
led = 3

grovepi.pinMode(led,"OUTPUT")

# Set up the Ultrasonic Ranger
UltrasonicPORT = 4 

# Set up the button
button = 2
grovepi.pinMode(button,"INPUT")

# Set up locks
lock = threading.Lock()

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("talisejessica/led")
    client.message_callback_add("talisejessica/led", led_callback)
    client.subscribe("talisejessica/lcd")
    client.message_callback_add("talisejessica/lcd", lcd_callback)


# Custom callbacks.
def led_callback(client, userdata, msg):
    # Turn on or off LED
    if str(msg.payload, "utf-8") == "LED_ON":
        with lock:
            grovepi.digitalWrite(led, 1)
    elif str(msg.payload, "utf-8") == "LED_OFF":
        with lock:
            grovepi.digitalWrite(led, 0)
    else:
        print("Not a valid LED message")

def lcd_callback(client, userdata, msg):
    # Check and then send letter to lcd
    if str(msg.payload, "utf-8") is 'a' or 'w' or 's' or 'd':
        try:
            with lock:
                setText_norefresh(str(msg.payload, "utf-8"))
        except:
            print("Too many LCD messages at once")
    else:
        print("Not a valid LCD message")



if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    # client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    while True:
        # print("delete this line")
        
        # Read ultrasonic ranger
        distance = grovepi.ultrasonicRead(UltrasonicPORT)
        
        # Send a publish 
        client.publish("talisejessica/ultrasonicRanger", str(distance))

        # check the button
        press = grovepi.digitalRead(button)
        # Send message if button is pressed
        if press == 1:
            client.publish("talisejessica/button", "Button pressed!")
        




        time.sleep(1)
            

