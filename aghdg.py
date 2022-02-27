from concurrent.futures import thread
from re import T
import threading
from time import sleep
import tkinter as tk
import random
from dfsdfs import TETRIS_LEL, TETRIS_LINE, TETRIS_SQUARE, TETRIS_TEE, Game, BLOCK_SIZE, TETRIS_SKEW

game = Game()

class Block():
    def __init__(self, root: tk.Tk, host: Game, block):
        # Generate a 2D array to match the tetris array
        self.windows = [[None for i in range(len(block[1]))] for k in range(len(block))]
        self.game = host

        root.withdraw()
        root.deiconify()

        for i, k in enumerate(zip(*block)):
            for j, g in enumerate(k):
                if g == 1:
                    cWin = tk.Toplevel()
                    cWin.bind("<KeyPress>", self.keydown)
                    cWin.bind("<KeyRelease>", self.keyup)
                    canvas = tk.Canvas(cWin, height=BLOCK_SIZE, width=BLOCK_SIZE)
                    text = tk.Text(canvas)
                    text.insert(1.0, str("{0}, {1}".format(i, j)))
                    canvas.pack()
                    text.pack()

                    cWin.geometry("{0}x{0}+{1}+{2}".format(BLOCK_SIZE, i * (BLOCK_SIZE * 2), j * (BLOCK_SIZE * 2)))

                    self.windows[j][i] = cWin

    def keyup(self, e: tk.Event):
        pass
    
    def get_first_window(self) -> tuple:
        for i, k in enumerate(zip(*self.windows)):
            for j, l in enumerate(k):
                if l != None:
                    return (l), (i, j)
        return None

    def get_last_window(self) -> tuple:
        lastGood = None

        for i, j in enumerate(zip(*self.windows)):
            for k, m in enumerate(j):
                if m != None:
                    lastGood = (m), (i, k)
        return lastGood

    def get_location(self):
        curX = self.get_first_window()[0].winfo_x()
        curY = self.get_last_window()[0].winfo_y()

        return curX, curY

    def get_2D_location(self):
        curX, curY = self.get_location()

        return curX // BLOCK_SIZE, curY // BLOCK_SIZE

    def keydown(self, e: tk.Event):

        if (game.current_block == self):
            curX, curY = self.get_2D_location()
            firstWin, firstIndex = self.get_first_window()
            lastWin, lastIndex = self.get_last_window()
            
            if e.char.lower() == "x":
                pass

            elif e.keysym == "Right" or e.keysym == "Left":
                if e.keysym == "Right":
                    mod = BLOCK_SIZE * 2
                elif e.keysym == "Left":
                    mod = -(BLOCK_SIZE * 2)

                if ((lastWin.winfo_x() + mod + BLOCK_SIZE > game.screensize[0]) or (firstWin.winfo_x() + mod < 0)):
                    return

                
                for i in self.windows:
                    for k in i:
                        if k:
                            currX = k.winfo_x()
                            currY = k.winfo_y()
                            k.geometry("{0}x{0}+{1}+{2}".format(BLOCK_SIZE, (currX + mod), currY))
            else:
                if e.keysym == "Down":
                    mod = BLOCK_SIZE * 2

                    if ((firstWin.winfo_y() + (BLOCK_SIZE) + mod > game.screensize[1])):
                        return

                    for i in self.windows:
                        for k in i:
                            if k:
                                currX = k.winfo_x()
                                currY = k.winfo_y()
                                k.geometry("{0}x{0}+{1}+{2}".format(BLOCK_SIZE, currX, (currY + mod)))
            
            curX, curY = self.get_location()

            if (curX >= self.game.bottom[0] or curY >= self.game.bottom[1]):
                next_block()

def next_block():

    shapes = [TETRIS_SKEW, TETRIS_SQUARE, TETRIS_TEE, TETRIS_LEL, TETRIS_LINE]

    game.add_block(Block(ws, game, shapes[random.randrange(0, len(shapes))]))

def game_loop(game:Game):
    while True:
        # create list of coords in one block

        for i in game.current_block.windows:
            for k in i:
                if k:
                    
                    collided = False
                    currX = k.winfo_x()
                    currY = k.winfo_y()
                    print(currX,currY)

                    if (currY + BLOCK_SIZE*2 >= (game.bottom[1])):
                        collided = True
                    
                    else:
                        otherBlocks = []

                        for block in game.blocks:
                            if block != game.current_block:
                                for window in block.windows:
                                        for u in window:
                                            if window != u:
                                                if u:
                                                    print("main:",(currX,currY),"secondary:",(u.winfo_x(),u.winfo_y()))

                                                    collided = u.winfo_y() >= currY and u.winfo_y() <= currY + BLOCK_SIZE
                                                    collided |= u.winfo_x() >= currX and u.winfo_x()  <= currX + BLOCK_SIZE

                                                    assert(u != k)
                                                    assert(collided == False)

                    
                                        
                                        
        
        if not collided:
            for i in game.current_block.windows:
                for k in i:
                    if k:
                        currX = k.winfo_x()
                        currY = k.winfo_y()
                        k.geometry("{0}x{0}+{1}+{2}".format(BLOCK_SIZE, (currX), currY + (BLOCK_SIZE*2)))
        else:
            next_block()
        sleep(1)
        

if __name__ == "__main__":

    ws = tk.Tk()

    blocks = Block(ws, game, TETRIS_SQUARE)
    game.add_block(blocks)

    t = threading.Thread(target=game_loop, args=(game,))
    t.start()
    ws.mainloop()