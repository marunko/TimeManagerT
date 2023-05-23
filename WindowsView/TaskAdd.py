from tkinter import *


class AddWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Add Task")
        self.geometry("200x50")
        label = Label(self, text="This is a new Window")
        label.pack()

