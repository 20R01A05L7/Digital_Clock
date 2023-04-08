from tkinter import Tk
from tkinter import Label
import time
root = Tk()
root.title("Digital Clock")
def present_time():
    display_time = time.strftime("%I:%M:%S %p")
    d_clock.config(text=display_time)
    d_clock.after(200,present_time)
d_clock = Label(root, font=("arial",80),background="black",foreground="white")
d_clock.pack(anchor="center")
present_time()
root.mainloop()
