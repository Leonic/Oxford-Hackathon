import ctypes
import threading

BLOCK_SIZE = 64

TETRIS_SQUARE = [
    [0,0,0],
    [0,0,0],
    [0,1,1],
    [0,1,1]
]

TETRIS_LINE = [
    [0,0,1],
    [0,0,1],
    [0,0,1],
    [0,0,1]
]

ALT = list(zip(*TETRIS_LINE))

TETRIS_TEE = [
    [0,0,0],
    [0,0,0],
    [0,1,0],
    [1,1,1]
]

TETRIS_LEL = [
    [1,0,0],
    [1,0,0],
    [1,0,0],
    [1,1,1]
]


TETRIS_SKEW = [
    [0,0,0],
    [0,0,0],
    [0,1,1],
    [1,1,0]
]

class Game():
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.screensize = self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1)
        self.grid = [[None for i in range(self.screensize[0] // BLOCK_SIZE)] for k in range(self.screensize[1] // BLOCK_SIZE)]
        self.current_block = None
        
    def create_block(self):
        pass
    def on_tick(self):
        pass
    def rotate_block(self):
        pass


if __name__ == "__main__":
    game = Game()