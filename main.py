# This is a sample Python script.
from threading import Thread
from tkinter import *
import time

from Director import Director

class WW:

    def __init__(self, root, methodPlay, methodStop):
        self.methodPlay = methodPlay
        self.methodStop = methodStop
        self.b = Button(root, text="Play", command=self.methodPlay)
        self.b.pack()
        time.gmtime(1)

    def Pl(self):
        self.b.config(text="Stop",command=self.methodStop)

    def St(self):
        self.b.config(text="Play", command=self.methodPlay)

class Lbl:
    def __init__(self, root, t):
        self.time = t
        self.l = Label(root, text=t)
        self.l.pack()

    def updateL(self, t):
        self.time = t
        self.l.config(text= self.time)


class MainW:
    isCounting = False

    def __init__(self, root):
        self.time1 = 1
        self.w = WW(root, self.startCounting, self.stopCounting)
        self.l = Lbl(root, self.time1)

    def startCounting(self):
        t1 = Thread(target=self.counting)
        t1.start()

    def stopCounting(self):
        self.isCounting = False
        self.w.St()

    def counting(self):
        self.isCounting = True
        self.w.Pl()

        while self.isCounting:
            self.time1 += 1
            self.l.updateL(time.ctime())
            time.sleep(1)



if __name__ == '__main__':

    d = Director()

# frames place in specified x-y rel 0.3, 0.1, 0.6
    #sub frame1, 2 place
    # task list grid
   # root = Tk()
    #root.geometry("400x400")
    #m = MainW(root)

    #root.mainloop()


