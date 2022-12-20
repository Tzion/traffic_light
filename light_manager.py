import asyncio
import enum


def start_traffic_light():
    set_color_

if __name__ == "__main__":
    asyncio.run(start_traffic_light())

    
class Color(enum.Enum):
    RED = "red"
    GREEN = "green"
    

class TrafficLight:
    
    def __init__(self, initial_color=Color.RED):
        self.color = initial_color

        