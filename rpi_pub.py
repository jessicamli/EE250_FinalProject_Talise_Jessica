# To be run on the raspberry pi device
# communicates with the computer via MQTT

import paho.mqtt.client as mqtt
import time
import sys
import threading
from read_sensors import read_sensors


# Set up locks
lock = threading.Lock()

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))



if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    # client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    while True:
        # Read ultrasonic ranger
        distance = read_sensors()
        
        # Send a publish 
        client.publish("talisejessica/ultrasonicRanger1", str(distance[0]))
        client.publish("talisejessica/ultrasonicRanger2", str(distance[1]))

        time.sleep(1)
            

