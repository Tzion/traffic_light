import RPi.GPIO as GPIO
from enum import Enum
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

DETECTION_DISTANCE = 500.0 #  in centimeters - closer than that means thaere's a detection
ERROR_DISTANCE = 0

 
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
    print(f'distance read={distance}')
    if distance < ERROR_DISTANCE:
        raise Exception(f"bad reading of measurement senser: {distance}")
    if distance < DETECTION_DISTANCE:
        return 1
    else:
        return -1


def sensor_works():
    try:
        for _ in range(100):
            is_detected()
    except:
        print('distance sensor failed')
        return False
    return True
        

def wait_till_detection(threshold, waiting_sec):
    detected = 0
    while True:
        detected += is_detected()
        print(f'wait_till_detection detected: {detected} out of {threshold}')
        time.sleep(waiting_sec)
        if detected > threshold:
            return True
        if detected < 0:
            detected = 0

    
def test_wait_till_detection(threshold, waiting_sec):
    try:
        while True:
            print(f'Waiting for {threshold} detections with waiting time {waiting_sec} sec in between)')
            wait_till_detection(threshold, waiting_sec)
            print("detection finished")
 
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
    test_wait_till_detection(6, 1)

