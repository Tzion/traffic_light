import RPi.GPIO as GPIO
from enum import Enum
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def measure():
    FunctionStartTime = time.time()
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        if StartTime - FunctionStartTime > 0.1:
            return -1
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        if StopTime - FunctionStartTime > 0.1:
            return -1
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 

def is_detected():
    distance = measure()
    if distance < 1:
        raise Exception(f"bad reading of measurement senser: {distance}")
    if distance < 500:
        return True
    else:
        return False


def wait_till_detection(threshold, waiting_sec):
    detected = 0
    while True:
        detected += is_detected()
        time.sleep(waiting_sec)
        if detected > threshold:
            return True

    
def test_wait_till_detection():
    try:
        while True:
            wait = wait_till_detection(10, 1)
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
    

def test_measure_reads():
    try:
        while True:
            dist = measure()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()


if __name__ == '__main__':
    threshold = 6
    waiting_sec = 1
    print(f'Waiting for {threshold} detection with waiting time of {waiting_sec})')
    test_wait_till_detection(threshold, waiting_sec)

