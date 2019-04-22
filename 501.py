'''
Created on Apr 22, 2019

@author: Francesca
'''
from tkinter import *

root = Tk()


import random

counter = 0

mynumlist = []

while counter < 10:
    mynumlist.append(random.randint(1,100))
    counter = counter + 1
    
def average(array):
    List = Label(root, text = array)
    List.pack()
    ans = sum(array)/ len(array)
    Ans = Label(root, text = str(ans))
    Ans.pack()
   
   
ClickMe = Button(root, text="ClickMe", command=lambda:average(mynumlist))

ClickMe.pack()   
   
root.mainloop() 