import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger and button topics here
    client.subscribe("talisejessica/ultrasonicRanger1")
    client.message_callback_add("talisejessica/ultrasonicRanger1", ultrasonic_1_callback)
    client.subscribe("talisejessica/ultrasonicRanger2")
    client.message_callback_add("talisejessica/ultrasonicRanger2", ultrasonic_2_callback)


# Custom callbacks
def ultrasonic_1_callback(client, userdata, msg):
    # print out the distance from the ultrasonic Ranger
    print("First Distance: " + str(msg.payload, "utf-8") + " cm")

def ultrasonic_2_callback(client, userdata, msg):
    # print out the distance from the ultrasonic Ranger
    print("Second Distance: " + str(msg.payload, "utf-8") + " cm")



if __name__ == '__main__':
    client = mqtt.Client()
    # client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)
            

