from media_manager import MediaManager
from traffic_light import Color, TrafficLight
from distance_sensor import wait_till_detection, sensor_works
import random
import time


def setup():
    global traffic_light, media_manager
    traffic_light = TrafficLight()
    media_manager = MediaManager()


def run_flow():
    if sensor_works():
        run_flow_with_sensor()
    else:
        run_flow_no_sensor()


def run_flow_no_sensor():
    traffic_light.set_color(Color.RED)
    traffic_light.go_crazy()
    play_red()
    halt()
    play_green()


def run_flow_with_sensor():
    while True:
        traffic_light.set_color(Color.GREEN)
        try:
            wait_till_detection(9, 1)
        except Exception as e:
            print(e)
            return
        play_red()
        time.sleep(8)
        play_green()


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
            
