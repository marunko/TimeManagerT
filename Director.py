# instantiates all classes window
from tkinter import *
from WindowsView.MainWindow import *

class Director:
    def __init__(self):
        self.startTk()

        self.mainWindow = MainWindow(self.root)

        self.root.mainloop()
        print("after loop")

    def startTk(self):
        self.root = Tk()
        self.root.title("Time Manager")
        self.root.geometry("500x800")


    # load windows