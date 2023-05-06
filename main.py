# This is a sample Python script.
from tkinter import *
from Director import Director

def destroyW(frame, b):
    frame.destroy()
    b.pack()
    return b

if __name__ == '__main__':

    d = Director()
# frames place in specified x-y rel 0.3, 0.1, 0.6
    #sub frame1, 2 place
    # task list grid


