from time import *

class CounterManager:

    def __init__(self):
        self.__maxActivityTime = 50400 # 14 hours
        self.__maxAwakeTime = 90000 # 01 am next day (25h)

        #unchengable constant
        self.activityEndTime = 0 # ActivityTime seconds + current or 1am time in seconds ->save in file

        self.ActivityTime = 0  # set time left before activityEndTime 25 - open hour (6-24)
        # if 22-06 set no time left for today and reset

        self.taskTime = 0
        self.workTime = 0

    def resetCurrentTask(self, newtime):
        self.CurrenttaskTime = newtime


    def countingDownTask(self):

        self.CurrenttaskTime -= 1
        #sleep(0.5)

    def countingDownActivity(self):


        return

#time setters
    def setActivityTime(self):
        print(localtime().tm_hour, localtime().tm_min, localtime().tm_sec)
        currentDayTime = localtime().tm_hour*3600+localtime().tm_min*60+localtime().tm_sec
        #hours = int(currentDayTime/3600)
        #minutes = int((currentDayTime-(hours*3600))/60)
        #seconds = currentDayTime-((hours*3600)+(minutes*60))
        print(currentDayTime)
        #print(str(hours) + " " + str(minutes) + " "+str(seconds))

        #check all on new date (8 hour pass after prev session? session active?)
        if self.isANewDate:
            if(currentDayTime+self.__maxActivityTime > self.__maxAwakeTime):
                self.ActivityTime = self.__maxAwakeTime-currentDayTime
                self.activityEndTime = self.ActivityTime+time()

            elif(currentDayTime+self.__maxActivityTime < self.__maxAwakeTime):
                self.ActivityTime = self.__maxAwakeTime+currentDayTime
                self.activityEndTime = self.ActivityTime + time()
        else:
        #continue this date session
            self.ActivityTime = self.activityEndTime-time() # uploaded from file
            return

        #1 count end time  time()+resTime()
        #2 every 500mls update AT
        return

    def isANewDate(self):

        #8 hour pass after prev session?

            #is out of working time ? 01-06: set time 0 and dont save to file

        #session active?

        return False

    def clockTimeCounter(self):
        # clock every 1/2 sec
        return
    def EventMonthUpdate(self):
        #every sec update in sep thread
        return

#test
c = CounterManager()
#print(c.activityEndTime)
c.setActivityTime()