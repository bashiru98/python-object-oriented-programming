import random
import string
from tkinter import *



def rand_password():
    password = []
    for i in range(5):
        lets = random.choice(string.ascii_letters)
        symbs = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.append(lets)
        password.append(symbs)
        password.append(numbers)
    y = "".join(str(x) for x in password)
    trt.config(text=y)





root = Tk()
root.geometry("240x200")
bott = Button(root, text="generate password",command=rand_password)
bott.grid(row=2, column=2)
trt = Label(root, font=("times", 15, "bold"))
trt.grid(row=4, column=2)
root.mainloop()
