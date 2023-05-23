from tkinter import *
import numpy

class CounterWidget:
    def __init__(self, root):
        self.mainEventProgress = Label(root, text="Y progress")
        self.mainEventProgress.grid(row=0, column=0)
        self.monthProgress = Label(root, text="M progress")
        self.monthProgress.grid(row=1, column=0)
        self.activity = Label(root, text="Activity progress")
        self.activity.grid(row=2, column=0)
        self.workProgree = Label(root, text="Work progress")
        self.workProgree.grid(row=3, column=1)