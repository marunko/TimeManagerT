from tkinter import *
from WindowsView.SubWindows.TaskList import *
from Managers.CountersManager import *

class MainWindow:
    isCounting = False

    def __init__(self, root):
        self.counterManager = CounterManager()
        self.root = root
        self.frameCounters = Frame(self.root, bg="blue")
        self.frameTasks = Frame(self.root,bg="blue")
        self.frameCounters.place(relx = 0.0, rely = 0.0,relwidth = 1, relheight = 0.4)
        Label( self.frameCounters, bg="blue").pack(fill = BOTH, expand = True)
        self.frameTasks.place(relx = 0.01, rely = 0.4)
        #Button(self.frameTasks, text="DO").grid(row=0, column=0)

        self.taskList = TaskList(self.frameTasks, self.counterManager)


        return

    def uploadWidgets(self):

        return