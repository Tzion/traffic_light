from media_manager import MediaManager
from traffic_light import Color, TrafficLight
import random
import time


def setup():
    global traffic_light, media_manager
    traffic_light = TrafficLight()
    media_manager = MediaManager()

def run_flow():
    while True:
        play_red()
        play_green()
        traffic_light.set_color(Color.RED)
        halt()

def play_red():
    traffic_light.set_color(Color.RED)
    media_manager.play(Color.RED)

def play_green():
    traffic_light.set_color(Color.GREEN)
    media_manager.play(Color.GREEN)

def halt():
    delay_sec = random.random() * 3 * 60
    print(f'sleeping for {delay_sec:.2f} seconds')
    time.sleep(delay_sec)
    

if __name__ == "__main__":
    while True:
        setup()
        try:
            run_flow()
        except Exception as e:
            print(e)
            continue  # rerun setup in case of error
            
