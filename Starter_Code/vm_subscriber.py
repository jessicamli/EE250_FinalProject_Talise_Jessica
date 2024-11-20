"""EE 250L Lab 04 Starter Code

Group Members: Talise Baker-Matsuoka and Jessica Li
GitHub Link: https://github.com/usc-ee250-fall2024/mqtt-talise-and-jessica.git

Run vm_subscriber.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger and button topics here
    client.subscribe("talisejessica/ultrasonicRanger")
    client.message_callback_add("talisejessica/ultrasonicRanger", ultrasonic_callback)
    client.subscribe("talisejessica/button")
    client.message_callback_add("talisejessica/button", button_callback)


# Custom callbacks.
def ultrasonic_callback(client, userdata, msg):
    # print out the distance from the ultrasonic Ranger
    print("VM: " + str(msg.payload, "utf-8") + " cm")
def button_callback(client, userdata, msg):
    # check and then print out the button message
    if str(msg.payload, "utf-8") == "Button pressed!":
        print(str(msg.payload, "utf-8"))
    else:
        print("Incorrect button message")


if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    # client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    while True:
        #print("delete this line")
        time.sleep(1)
            

