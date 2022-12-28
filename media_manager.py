from os import listdir
from os.path import isfile, join
from traffic_light import Color
import random
import pygame

MEDIA_LIB = "./media"

class MediaManager:

    def __init__(self, lib = MEDIA_LIB):
        self.reds = self.load_files(lib + "/red")
        self.greens = self.load_files(lib + "/green")

    def load_files(self, path):
        files = [join(path,f) for f in listdir(path) if isfile(join(path, f))]
        files.sort()
        print(f'{len(files)} files were loaded from {path}')
        return files
    
    def play(self, color: Color):
        try:
            if color == Color.GREEN:
                track = random.sample(self.greens, 1)[0]
            else:
                track = random.sample(self.reds, 1)[0]
            RaspberyPlayer.play_track(track)
        except Exception as e:
            print(e)
            RaspberyPlayer.stop_track(track)
        
        

class RaspberyPlayer():
    
    def play_track(track):
        print(f'playing track {track}')
        pygame.mixer.init()
        pygame.mixer.music.load(track)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pass

    def stop_track(track):
        pygame.mixer.music.stop()
            

