import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_threshold = 350  # change this value
sound_threshold = 600 # Experiment performed in loud room so number is high


def blink_led(pin, frequency, num_times):
  for i in range(0, num_times, 1):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(frequency) 
    GPIO.output(pin, GPIO.LOW)
    time.sleep(frequency) 


while True: 
  time.sleep(0.5) 

  # Blink the LED 5 times every 500 ms
  blink_led(chan_list, 0.5, 5)

  # Read the light output for 5 seconds
  for j in range(0, 50, 1):
    # get reading from adc on the light sensor
    lightness = mcp.read_adc(0)
    print("Raw Value: " + str(lightness))
    if lightness < lux_threshold:
      print("Dark")
    else:
      print("Bright")
    time.sleep(0.1)

  # Blink the LED 4 times every 200 ms
  blink_led(chan_list, 0.2, 4) 
  
  # Read the sound output for 5 seconds
  for l in range(0, 50, 1):
    led_on = 0
    # get reading from adc on the sound sensor
    sound = mcp.read_adc(1)
    print("Raw Value: " + str(sound))
    if sound < sound_threshold:
      led_on = 0
    else:
      led_on = 1
    if led_on == 1:
      GPIO.output(chan_list, GPIO.HIGH)
    else:
      GPIO.output(chan_list, GPIO.LOW)
    time.sleep(0.1)
