from enum import Enum
import RPi.GPIO as GPIO

RED_PIN = 3
GREEN_PIN = 5

class Color(Enum):
    RED = 0
    GREEN = 1
    
class TrafficLight:

    def __init__(self, initialColor=Color.RED):
        self.color = initialColor
    
    
    def set_color(self, color: Color):
        print(f'setting color to {color})')
        self.color = color
        set_gpios(color)

def set_gpios(color_on):
    if color_on == Color.RED:
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.LOW)
    if color_on == Color.GREEN:
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        GPIO.output(RED_PIN, GPIO.LOW)
        
