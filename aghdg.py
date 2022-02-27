import tkinter as tk
from dfsdfs import Game, BLOCK_SIZE

game = Game()

class Block():
    def __init__(self, root: tk.Tk):
        self.windows = []

        root.withdraw()
        root.deiconify()

        for i in range(3):
            cWin = tk.Toplevel()
            cWin.bind("<KeyPress>", self.keydown)
            cWin.bind("<KeyRelease>", self.keyup)
            canvas = tk.Canvas(cWin, height=BLOCK_SIZE, width=BLOCK_SIZE)
            canvas.pack()

            cWin.geometry("{0}x{0}+{1}+0".format(BLOCK_SIZE, i * (BLOCK_SIZE * 2)))

            self.windows.append(cWin)

        self.windows[0].focus_set()

    def keyup(self, e: tk.Event):
        pass
    
    def get_location(self):
        curX = self.windows[0].winfo_x()
        curY = self.windows[len(self.windows) - 1].winfo_y()

        return curX, curY

    def keydown(self, e: tk.Event):
        lastWin = lastWinPos = mod = 0

        if e.char.lower() == "x":
            print(self.get_location())

        elif e.keysym == "Right" or e.keysym == "Left":
            if e.keysym == "Right":
                mod = BLOCK_SIZE

                lastWin = self.windows[len(self.windows) - 1]
                lastWinPos = lastWin.winfo_x() 

            elif e.keysym == "Left":
                mod = -BLOCK_SIZE

                lastWin = self.windows[0]
                lastWinPos = lastWin.winfo_x() 

            if (((lastWinPos + (BLOCK_SIZE * 2)) + mod > game.screensize[0]) or (lastWinPos + mod < 0)):
                return

            for i, k in enumerate(self.windows):
                curX = k.winfo_x()
                curY = k.winfo_y()

                k.geometry("{0}x{0}+{1}+{2}".format(BLOCK_SIZE, (curX + mod), curY))
        else:
            if e.keysym == "Down":
                mod = BLOCK_SIZE

                lastWin = self.windows[0]
                lastWinPos = lastWin.winfo_y() 

                if ((lastWinPos + BLOCK_SIZE + mod > game.screensize[1])):
                    return

                for i, k in enumerate(self.windows):
                    curX = k.winfo_x()
                    curY = k.winfo_y()

                    k.geometry("{0}x{0}+{1}+{2}".format(BLOCK_SIZE, curX, (curY + mod)))


if __name__ == "__main__":

    ws = tk.Tk()

    blocks = Block(ws)


    ws.mainloop()