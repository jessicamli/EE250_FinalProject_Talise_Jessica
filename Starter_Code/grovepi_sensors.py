""" EE 250L Lab 02: GrovePi Sensors

Talise Baker-Matsuoka and Jessica Li

Insert Github repository link here.
https://github.com/usc-ee250-fall2024/lab-02-grovepi-sensors-TaliseBakerM
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
import grovepi
from grove_rgb_lcd import *

# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')



"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
  UltrasonicPORT = 4    # D4

  # Connect the Grove Rotary Angle Sensor to analog port A0
  potentiometer = 0  #A0

  # Set the potentiometer pin to an input
  grovepi.pinMode(potentiometer,"INPUT")

  # Holds last text displayed on the LCD
  prev_text = ""


  while True:
    #So we do not poll the sensors too quickly which may introduce noise,
    #sleep for a reasonable time of 200ms between each iteration.
    time.sleep(0.2)
    

    try: 
      # Read sensor value from potentiometer
      sensor_value = grovepi.analogRead(potentiometer)
      # Read the ultrasonic sensor
      distance = grovepi.ultrasonicRead(UltrasonicPORT)
      
      sensor_str = ""
      if sensor_value < 10:
        sensor_str = "   " + str(sensor_value)
      elif sensor_value < 100:
        sensor_str = "  " + str(sensor_value)
      elif sensor_value < 1000:
        sensor_str = " " + str(sensor_value)
      else:
        sensor_str = str(sensor_value)
      
      dist_str = ""
      if distance < 10:
        dist_str = "  " + str(distance)
      elif distance < 100:
        dist_str = " " + str(distance)
      else:
        dist_str = str(distance)
     

      # Set the lcd to the correct values
      if distance < sensor_value:
        # Set the text with sensor value, obj press, and distance
        new_text = sensor_str + "cm OBJ PRES \n" + dist_str + "cm"
      else:
        # Set the text with sensor value and distance
        new_text = sensor_str + "cm          \n" + dist_str + "cm"

      # To prevent LCD flashing, only update the LCD display if the text has changed
      if new_text != prev_text:
        setText_norefresh(new_text)
        prev_text = new_text

    except IOError:
      print("Error")

