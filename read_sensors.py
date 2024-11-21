# read_sensors contains a function that reads the raspberry pi sensors using the grovepi functions

import sys
import time
import grovepi

sys.path.append('../../Software/Python/')

def read_sensors():
  UltrasonicPORT_1 = 4    # D4 port for the first ultrasonic sensor
  UltrasonicPORT_2 = 5 # Not sure which one yet
  dist1 = 0
  dist2 = 0


  try: 
    # Read the first ultrasonic sensor
    dist1 = grovepi.ultrasonicRead(UltrasonicPORT_1)

    # wait a small amount of time to prevent any interference
    time.sleep(0.2)

    # Read the second ultrasonic sensor
    dist2 = grovepi.ultrasonicRead(UltrasonicPORT_2)
      
  except IOError:
    print("Error")

  distance = [dist1, dist2]

  return distance

