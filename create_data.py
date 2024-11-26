# create_data.py collects data into a csv file to use to train the model

import pandas as pd
import local_sub
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
    # print("First Distance: " + str(msg.payload, "utf-8") + " cm")
    # Save the distance
    global sensor_dist1
    sensor_dist1 = int(msg.payload)


def ultrasonic_2_callback(client, userdata, msg):
    # print out the distance from the ultrasonic Ranger
    # print("Second Distance: " + str(msg.payload, "utf-8") + " cm")
    # Save the distance
    global sensor_dist2
    sensor_dist2 = int(msg.payload)

if __name__ == '__main__':
    client = mqtt.Client()
    # client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    # Assign labels for the elements 
    # The two distances come first followed by the correct location on the grid
    labels = ['dist1', 'dist2', 'location']  

    while True:
        while connection != 0:
            time.sleep(1)

        # Request User input for the square the object is placed
        square = input("Please enter the square: ")
        time.sleep(1)
        dist = [sensor_dist1, sensor_dist2, int(square)]

        # Add the distance and correct label to the csv file
        distance = dict(zip(labels, dist)) 
        data = pd.DataFrame([distance])
        data.to_csv('distances.csv', mode='a', header=False, index=False)


        time.sleep(1)



