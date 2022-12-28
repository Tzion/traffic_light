from enum import Enum
import RPi.GPIO as GPIO
import time

RED_PIN = 2
GREEN_PIN = 3

class Color(Enum):
    RED = 0
    GREEN = 1
    
class TrafficLight:

    def __init__(self, initialColor=Color.RED):
        self.color = initialColor
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RED_PIN, GPIO.OUT)
        GPIO.setup(GREEN_PIN, GPIO.OUT)
        # self.test_all_gpios()
    
    def test_all_gpios(self):
        for pin in range(0,20):
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 1)
            print(f'pin {pin} is on')
            time.sleep(0.4)
            GPIO.output(pin,0) 
        
    
    def set_color(self, color: Color):
        print(f'setting color to {color})')
        self.color = color
        set_gpios(color)

def set_gpios(color_on):
    if color_on == Color.RED:
        GPIO.output(RED_PIN, GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output(GREEN_PIN, GPIO.LOW)
    if color_on == Color.GREEN:
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output(RED_PIN, GPIO.LOW)
        
