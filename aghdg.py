import tkinter as tk
from dfsdfs import Game, BLOCK_SIZE, TETRIS_SKEW

game = Game()

class Block():
    def __init__(self, root: tk.Tk, host: Game, block):
        # Generate a 2D array to match the tetris array
        self.windows = [[None for i in range(len(block[1]))] for k in range(len(block))]
        self.game = host

        root.withdraw()
        root.deiconify()

        for i, k in enumerate(block):

            for j, g in enumerate(k):
                if g == 1:
                    cWin = tk.Toplevel()
                    cWin.bind("<KeyPress>", self.keydown)
                    cWin.bind("<KeyRelease>", self.keyup)
                    canvas = tk.Canvas(cWin, height=BLOCK_SIZE, width=BLOCK_SIZE)
                    canvas.pack()

                    cWin.geometry("{0}x{0}+{1}+{2}".format(BLOCK_SIZE, i * (BLOCK_SIZE * 2), j * (BLOCK_SIZE * 2)))

                    self.windows[i][j] = cWin

    def keyup(self, e: tk.Event):
        pass
    
    def get_first_window(self) -> tuple:
        for i, k in enumerate(self.windows):
            for j, l in enumerate(k):
                if l != None:
                    return (l), (i, j)
        return None

    def get_last_window(self) -> tuple:
        lastGood = None

        for i, j in enumerate(self.windows):
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
        curX, curY = self.get_2D_location()
        firstWin, firstIndex = self.get_first_window()
        lastWin, lastIndex = self.get_last_window()
        
        if e.char.lower() == "x":
            pass

        elif e.keysym == "Right" or e.keysym == "Left":
            if e.keysym == "Right":
                mod = BLOCK_SIZE

            elif e.keysym == "Left":
                mod = -BLOCK_SIZE

            if (((curX + (BLOCK_SIZE * len(self.windows[firstIndex[0]]))) + mod > game.screensize[0]) or (firstWin.winfo_x() + mod < 0)):
                return

            for i in self.windows:
                for k in i:
                    if k:
                        currX = k.winfo_x()
                        currY = k.winfo_y()
                        k.geometry("{0}x{0}+{1}+{2}".format(BLOCK_SIZE, (currX + mod), currY))
        else:
            if e.keysym == "Down":
                mod = BLOCK_SIZE

                if ((lastWin.winfo_y() + BLOCK_SIZE + mod > game.screensize[1])):
                    return

                for i in self.windows:
                    for k in i:
                        if k:
                            currX = k.winfo_x()
                            currY = k.winfo_y()
                            k.geometry("{0}x{0}+{1}+{2}".format(BLOCK_SIZE, currX, (currY + mod)))


if __name__ == "__main__":

    ws = tk.Tk()

    blocks = Block(ws, game, TETRIS_SKEW)


    ws.mainloop()