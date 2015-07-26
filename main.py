import Tkinter as tk
import winsound

froggy = "C:/Users/pataelmo/Downloads/Super Mario Bros 3 Real NES Sound Effects/Froggy Hop SFX.wav"
mario = "C:/Users/pataelmo/Downloads/Super Mario Bros 3 Real NES Sound Effects/Pipe Maze SFX.wav"

def onKeyPress(event):
    if event.char=='a':
        winsound.PlaySound(froggy,0)
    elif event.char=='s':
        winsound.PlaySound(mario,0)

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()