# This is a sample Python script.
from tkinter import *

class A:
    def __init__(self, d):
        print(1)
    def t(self):
        print("par")

class B(A):
    def __init__(self, d):
        print(2)



if __name__ == '__main__':
    #root = Tk()
    #root.title("Time Manager")
    #root.geometry("500x500")
    B(2).t()
    #root.mainloop()



