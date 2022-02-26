import tkinter as tk

def keyup(e):
    print ('up', e.char)
def keydown(e):
    print ('down', e.char)

def New_Window(ws: tk.Tk):
    wins = []

    ws.withdraw()
    ws.deiconify()

    for i in range(3):
        Window = tk.Toplevel()
        Window.bind("<KeyPress>", keydown)
        Window.bind("<KeyRelease>", keyup)
        canvas = tk.Canvas(Window, height=64, width=64)
        canvas.pack()

        Window.geometry("64x64+{}+0".format(i * 128))

        wins.append(Window)

    wins[0].focus_set()

    return wins

if __name__ == "__main__":

    ws = tk.Tk()

    blocks = New_Window(ws)

    ws.mainloop()