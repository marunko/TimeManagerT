

class CounterManager:

    def __init__(self):

        self.ActivityTime = 0


    def resetCurrentTask(self, newtime):
        self.CurrenttaskTime = newtime


    def countingDownTask(self):

        self.CurrenttaskTime -= 1
        #sleep(1)

    def countingDownActivity(self):
        return