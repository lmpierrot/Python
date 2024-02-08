import time
import pyautogui
import pyscreeze
import tkinter as tk

def screenchot():
    name = int(round(time.time() * 1000))
    name = 'C:/Users/marclp/OneDrive - Broward College/Python/screenshot data/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button =tk.Button(
    frame,
    text="Take Screenshot",
    command=screenchot
)
button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="QUIT",
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()