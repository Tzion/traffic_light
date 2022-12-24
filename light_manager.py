from media_manager import MediaManager
from traffic_light import Color, TrafficLight
import random
import time


def start_flow():
    while True:
        play_red()
        play_green()
        halt()

def play_red():
    traffic_light.set_color(Color.RED)
    media_manager.play_red()

def play_green():
    traffic_light.set_color(Color.GREEN)
    media_manager.play_green()


def halt():
    one_to_six_minutes_delay = 60.0 + random.random() * 5 * 60
    delay = one_to_six_minutes_delay
    time.sleep(delay)
    

if __name__ == "__main__":
    traffic_light = TrafficLight()
    media_manager = MediaManager()
    start_flow()
