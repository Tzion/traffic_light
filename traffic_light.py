from enum import Enum
# import RPi.GPIO as GPIO

class Color(Enum):
    RED = 0
    GREEN = 1
    
class TrafficLight:
    def __init__(self, initialColor):
        self.color = initialColor
    
    
    def set_color(self, color):
        print(f'setting color to ${color})')
        self.color = color
        # GPIO.

