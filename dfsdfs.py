import ctypes
import threading

BLOCK_SIZE = 64

class Game():
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.screensize = self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1)
        self.grid = [[None for i in range(self.screensize[0])] for k in range(self.screensize[1])]

    def create_block(self):
        pass
    def on_tick(self):
        pass
