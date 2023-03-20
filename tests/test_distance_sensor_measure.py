import time
from distance_sensor import measure
import RPi.GPIO as GPIO


if __name__ == '__main__':
    try:
        while True:
            dist = measure()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()