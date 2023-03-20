from os import listdir
from os.path import isfile, join
from traffic_light import Color
import random
import pygame

MEDIA_LIB = "./media"

class MediaManager:

    def __init__(self, lib = MEDIA_LIB):
        reds = self.load_files(lib + "/red")
        greens = self.load_files(lib + "/green")
        self.tracks = [couple for couple in zip(reds, greens)]
        self.cur_tracks = self.pick_track()

    def load_files(self, path):
        files = [join(path,f) for f in listdir(path) if isfile(join(path, f))]
        files.sort()
        print(f'{len(files)} files were loaded from {path}')
        return files

    def pick_track(self):
        return random.sample(self.tracks, 1)[0]
    
    def play(self, color: Color):
        if not self.cur_tracks or not self.cur_tracks[color.value]:
            self.cur_tracks = self.pick_track()
        try:
            track = self.cur_tracks[color.value]
            RaspberyPlayer.play_track(track)
        except Exception as e:
            print(e)
        
        

class RaspberyPlayer():
    
    def play_track(track):
        print(f'playing track {track}')
        freq = 44100    # audio CD quality
        bitsize = -16   # unsigned 16 bit
        channels = 2    # 1 is mono, 2 is stereo
        buffer = 2048   # number of samples (experiment to get right sound)
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.load(track)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pass
            

