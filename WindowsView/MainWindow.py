from tkinter import *
from WindowsView.SubWindows.TaskList import *
from Managers.CountersManager import *

class MainWindow:

    def __init__(self, root):
        self.counterManager = CounterManager()
        self.root = root
        self.frameCounters = Frame(self.root)
        self.frameTasks = Frame(self.root)
        self.frameCounters.pack()
        self.frameTasks.pack()
        #Button(self.frameTasks, text="DO").grid(row=0, column=0)

        self.taskList = TaskList(self.frameTasks)


        return

    def uploadWidgets(self):

        return