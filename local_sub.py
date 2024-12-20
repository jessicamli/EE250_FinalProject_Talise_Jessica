# Code to figure out and display what square the object is in. Yay!
# Type http://127.0.0.1:5000/ into browser to display
# Requires distmodel.h5 file

import paho.mqtt.client as mqtt
import time
from result_display_cli import send_to_http 
import numpy as np
from tensorflow.keras.models import load_model

# Define global variables to change later
sensor_dist1 = 0
sensor_dist2 = 0
connection = -1
square = 0

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
        

        # Load the model and figure out the predicted square
        dist1 = np.array([sensor_dist1])  
        dist2 = np.array([sensor_dist2])  

        input_data = np.stack([dist1, dist2], axis=-1)

        model = load_model('distmodel.h5')
        prediction = model.predict(np.array(input_data))
        #prediction = prediction.flatten()

        location = np.argmax(prediction)

        # The actual ordering from the output given is [2 0 1 3] so the order must be changed

        print(prediction)
        print(location)

        square = location + 1
        print(square)


        # This code sends to the http server and displays the data
        response = send_to_http(square)
        # Print the response from the server to check for erros
        if response.status_code == 200:
            print("Yay, you did it!")
        else:
            print("Not so great....", response.status_code)
   
        
        time.sleep(1)

