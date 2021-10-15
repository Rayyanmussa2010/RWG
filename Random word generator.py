# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:37:48 2021

@author: DELL
"""

from tkinter import *
import random

root=Tk()
root.title("Random Word Generator")
root.geometry("400x400")
list1=["A", "B", "C", "B", "D", "B", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
label1=Label(root)


def random_number():
    random_no1=random.randint(0, 25)
    random_no2=random.randint(0, 25)
    random_no3=random.randint(0, 25)
    random_no4=random.randint(0, 25)
    random_no5=random.randint(0, 25)
    random_alpha1=list1[random_no1]
    random_alpha2=list1[random_no2]
    random_alpha3=list1[random_no3]
    random_alpha4=list1[random_no4]
    random_alpha5=list1[random_no5]
    label1["text"]="The word is: "+random_alpha1+random_alpha2+random_alpha3+random_alpha4+random_alpha5
    
button1=Button(root, text="Generate random word", command=random_number)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)
label1.place(relx=0.5, rely=0.74, anchor=CENTER)













root.mainloop()