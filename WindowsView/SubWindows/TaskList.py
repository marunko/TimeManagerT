from tkinter import *
import numpy

class TaskList:
    def __init__(self, rootFrame):
        #self.taskRows = [None] * 5
        self.taskRows = numpy.empty(5, dtype=object)
        self.frame = Frame(rootFrame)
        self.frame.pack()
        for i in range(len(self.taskRows)):
            self.taskRows[i] = TaskRow(self.frame, i)





class TaskRow:

    def __init__(self, Pframe, id):
        self.rowFrame = Frame(Pframe);
        self.rowFrame.pack()
        self.id = Label(self.rowFrame, text=str(id))
        self.taskTitle = Label(self.rowFrame, text="Some task description")
        self.remove = Button(self.rowFrame, text="Button-{id}")

        self.id.pack()
        self.taskTitle.pack()
        self.remove.pack()