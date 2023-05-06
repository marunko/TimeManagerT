from tkinter import *
import numpy


class TaskRow:

    def __init__(self, pframe, id, remove, title, time, play):
        self.rowFrame = Frame(pframe)
        self.rowFrame.grid(row=id, column=0, padx=2, sticky="nsew")
        self.id = Label(self.rowFrame, text=str(id))
        self.taskTitle = Label(self.rowFrame, text=title)
        self.taskTime = Label(self.rowFrame, text=str(time))
        self.remove = Button(self.rowFrame, text="Button-" + str(id), command=lambda i=id:
        remove(i))
        if (id == 0):
            self.addPlayButton(play)

        self.id.grid(row=0, column=0)
        self.taskTitle.grid(row=0, column=1)
        self.taskTime.grid(row=0, column=2)
        self.remove.grid(row=0, column=3)

    def addPlayButton(self, play):
        self.play = Button(self.rowFrame, text="Play", command=play)
        self.play.grid(row=0, column=4)
        # PROGRESS BAR HERE

    def placeStopButton(self, stop):
        self.play.config(text="Stop", command=stop)

    def placePlayButton(self, play):
        self.play.config(text="Play", command=play)
    def getFrame(self):
        return self.rowFrame

    def getId(self):
        return self.id


# ---------------------------------------------------------------------------------------------------------
# -----------------------------------    TASKLIST
# ---------------------------------------------------------------------------------------------------------


class TaskList:

    # set dependency Fileloader class here

    def __init__(self, rootFrame, counterManager):
        # self.taskRows = [None] * 5
        # IN file remove task
        self.countermanager = counterManager
        self.taskRows = numpy.empty(5, dtype=Frame)
        self.frame = Frame(rootFrame)
        self.frame.pack()
        self.loadAllTasks()

    def loadAllTasks(self):
        # load title
        title = "Some title"
        taskTime = 222222
        for i in range(len(self.taskRows)):
            self.taskRows[i] = TaskRow(self.frame, i, self.removeTask, title, taskTime, self.Play)

    # EVENTS BUTTONS

    def removeTask(self, id):

        self.taskRows[id].getFrame().destroy()
        self.taskRows[id] = None
        # remove in file

        # rewrite array
        newArray = numpy.empty(len(self.taskRows) - 1, dtype=Frame)
        j = 0
        for i in range(len(self.taskRows)):
            if (self.taskRows[i] != None):
                newArray[j] = self.taskRows[i]
                j += 1
        self.taskRows = newArray

        # change Rows location
        for i in range(len(self.taskRows)):
            if (i == 0):
                self.taskRows[i].addPlayButton(self.Play)
            self.taskRows[i].id.configure(text=str(i))
            self.taskRows[i].remove.configure(text="Button-" + str(i),
                                              command=lambda i=i: self.removeTask(i))

        return

    def Play(self):
        # downcount time being oriented to system time
        # replace button text and command to STOP
        self.taskRows[0].placeStopButton(self.Stop)
        return

    def Stop(self):
        self.taskRows[0].placePlayButton(self.Play)
        return
    # moving existing objects

    def upTask(self):

        # change ids label and buttons of two following rows
        # if set as 0 id then add button play and progress bar
        # change places in array
        return

    def downTask(self):
        # change ids label and buttons of two following rows
        # if set as 0 id then add button play
        # change places in array
        return

# update on new event adding new task
    def countDown(self):
        return