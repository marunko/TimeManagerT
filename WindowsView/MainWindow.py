from tkinter import *


from WindowsView.SubWindows.CounterWidget import CounterWidget
from WindowsView.SubWindows.TaskList import *
from Managers.CountersManager import *
from .TaskAdd import *

class MainWindow:
    isCounting = False

    def __init__(self, root):
        self.counterManager = CounterManager()
        self.root = root
        self.frameCounters = Frame(self.root, bg="blue")
        self.frameTasks = Frame(self.root,bg="#856ff8")
        # buttons Frame menu, add
        self.buttons = Frame(self.root, bg="green")

        self.frameCounters.place(relx = 0.01, rely = 0.0,relwidth = 1, relheight = 0.4)
        #Label( self.frameCounters, bg="blue").pack(fill = BOTH, expand = True)
        self.frameTasks.place(relx = 0.01, rely = 0.4, relwidth = 1, relheight = 0.5)
        #Button(self.frameTasks, text="DO").grid(row=0, column=0)
        self.buttons.place(relx = 0.01, rely = 0.9, relwidth = 1, relheight = 0.1)

        self.taskList = TaskList(self.frameTasks, self.counterManager)
        self.counterWidget = CounterWidget(self.frameCounters)
        self.ButtonsWidget()
        return

    def uploadWidgets(self):

        return
    def ButtonsWidget(self):
        self.addButton = Button(self.buttons,text="Add", bg="red", command=self.openAddWindow)
        self.configure = Button(self.buttons,text="Settings", bg="yellow")

        self.addButton.grid(row=0, column=1)
        self.configure.grid(row=0, column=2)

    def openAddWindow(self):
        self.addWindow = AddWindow()


