# Generic code to create a mqtt connection with the rpi

import paho.mqtt.client as mqtt
import time

sensor_dist1 = 0
sensor_dist2 = 0
connection = -1

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    global connection
    connection = rc

    #subscribe to the ultrasonic ranger and button topics here
    client.subscribe("talisejessica/ultrasonicRanger1")
    client.message_callback_add("talisejessica/ultrasonicRanger1", ultrasonic_1_callback)
    client.subscribe("talisejessica/ultrasonicRanger2")
    client.message_callback_add("talisejessica/ultrasonicRanger2", ultrasonic_2_callback)


# Custom callbacks
def ultrasonic_1_callback(client, userdata, msg):
    # print out the distance from the ultrasonic Ranger
    print("First Distance: " + str(msg.payload, "utf-8") + " cm")
    global sensor_dist1
    sensor_dist1 = int(msg.payload)


def ultrasonic_2_callback(client, userdata, msg):
    # print out the distance from the ultrasonic Ranger
    print("Second Distance: " + str(msg.payload, "utf-8") + " cm")
    global sensor_dist2
    sensor_dist2 = int(msg.payload)

def get_distance():
    distance = [sensor_dist1, sensor_dist2]
    print(sensor_dist1)
    return distance

if __name__ == '__main__':
    client = mqtt.Client()
    # client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    while True:
        while connection != 0:
            time.sleep(1)
            
        
        time.sleep(1)
