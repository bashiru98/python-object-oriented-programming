import tkinter as tk


def btnClick(num):
    global operator
    operator = operator + str(num)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator= ""
    text_input.set(operator)

def equalcom():
    global operator
    man=(eval(operator))
    text_input.set(man)
    operator= ""

def displayBudget(txt):
    global expression
    expression = expression + str(txt)
    budget_input.set(expression)

def btnClear():
    global expression
    expression= ""
    budget_input.set(expression)


root = tk.Tk()

operator = ""

text_input=tk.StringVar()

canvas = tk.Canvas(root, width=600, height=500)
canvas.pack()

frame = tk.Frame(root, bg='gray', bd=5)
frame.place(relx=0, rely=0, relheight=0.1, relwidth=0.1)

button1 = tk.Button(frame, text="1", font=50, command=lambda:btnClick(1))
button1.place(relx=0, rely=0, relheight=1, relwidth=1)

frame2 = tk.Frame(root, bg='gray', bd=5)
frame2.place(relx=0.105, rely=0, relheight=0.1, relwidth=0.1)

button2 = tk.Button(frame2, text="2", font=50,command=lambda:btnClick(2))
button2.place(relx=0, rely=0, relheight=1, relwidth=1)

frame3 = tk.Frame(root, bg='gray', bd=5)
frame3.place(relx=0.21, rely=0, relheight=0.1, relwidth=0.1)

button3 = tk.Button(frame3, text="3", font=50,command=lambda:btnClick(3))
button3.place(relx=0, rely=0, relheight=1, relwidth=1)

frame4 = tk.Frame(root, bg='gray', bd=5)
frame4.place(relx=0.315, rely=0, relheight=0.1, relwidth=0.1)

button4 = tk.Button(frame4, text="4", font=50,command=lambda:btnClick(4))
button4.place(relx=0, rely=0, relheight=1, relwidth=1)

frame5 = tk.Frame(root, bg='gray', bd=5)
frame5.place(relx=0.42, rely=0, relheight=0.1, relwidth=0.1)

button5 = tk.Button(frame5, text="5", font=50,command=lambda:btnClick(5))
button5.place(relx=0, rely=0, relheight=1, relwidth=1)

frame6 = tk.Frame(root, bg='gray', bd=5)
frame6.place(relx=0, rely=0.105, relheight=0.1, relwidth=0.1)

button6 = tk.Button(frame6, text="6", font=50,command=lambda:btnClick(6))
button6.place(relx=0, rely=0, relheight=1, relwidth=1)

frame7 = tk.Frame(root, bg='gray', bd=5)
frame7.place(relx=0.105, rely=0.105, relheight=0.1, relwidth=0.1)

button7 = tk.Button(frame7, text="7", font=50,command=lambda:btnClick(7))
button7.place(relx=0, rely=0, relheight=1, relwidth=1)

frame8 = tk.Frame(root, bg='gray', bd=5)
frame8.place(relx=0.21, rely=0.105, relheight=0.1, relwidth=0.1)

button8 = tk.Button(frame8, text="8", font=50,command=lambda:btnClick(8))
button8.place(relx=0, rely=0, relheight=1, relwidth=1)

frame9 = tk.Frame(root, bg='gray', bd=5)
frame9.place(relx=0.315, rely=0.105, relheight=0.1, relwidth=0.1)

button9 = tk.Button(frame9, text="9", font=50,command=lambda:btnClick(9))
button9.place(relx=0, rely=0, relheight=1, relwidth=1)

frame10 = tk.Frame(root, bg='gray', bd=5)
frame10.place(relx=0.42, rely=0.105, relheight=0.1, relwidth=0.1)

button10 = tk.Button(frame10, text="0", font=50,command=lambda:btnClick(0))
button10.place(relx=0, rely=0, relheight=1, relwidth=1)

#frame11 =tk.Frame(root, bg='gray', bd=5)
#frame11.place( relx=0.525,rely=1, relheight=0.105, width=0.1, anchor='e')

clear =tk.Button(root, text="c", font=50,bd=10,command=lambda:btnClearDisplay())
clear.place(relx=0, rely=0.21,relheight=0.1, relwidth=0.525)

addition=tk.Button(root,text="+", font=50,bd=10,command=lambda:btnClick('+'))
addition.place(relx=0,rely=0.315, relheight=0.1, relwidth=0.1)

subraction=tk.Button(root,text="-", font=50,bd=10,command=lambda:btnClick('-'))
subraction.place(relx=0.105,rely=0.315, relheight=0.1, relwidth=0.1)

div=tk.Button(root,text="/", font=50,bd=10,command=lambda:btnClick('/'))
div.place(relx=0.21,rely=0.315, relheight=0.1, relwidth=0.1)

mlt=tk.Button(root,text="*", font=50,bd=10,command=lambda:btnClick('*'))
mlt.place(relx=0.315,rely=0.315, relheight=0.1, relwidth=0.1)


try:
     eqt=tk.Button(root,text="=", font=50,bd=10,command=lambda:equalcom())
     eqt.place(relx=0.42,rely=0.315, relheight=0.1, relwidth=0.1)
except Exception:
      print('error')

budget_input=tk.StringVar()
expression = " "


mybdt=tk.Button(root,text="BUDGET", font=40,bd=10, command=lambda:displayBudget(
    'savings:   '
    
    'transportation:   '
    
    'food:   '
    
    'miscilenous: '
))
mybdt.place(relx=0.525,rely=0.315, relheight=0.1, relwidth=0.15)

entry = tk.Entry(root, bd=15, bg='lightgreen', textvariable=text_input, font=(' arial',20,'bold'))
entry.pack(side='bottom', fill='both')


entry2 =tk.Entry(root,bd=15, bg='lightgreen', font=(' arial',20,'bold'), textvariable=budget_input)
entry2.place(relx=0.53, rely=0, relwidth=0.47, relheight=0.31)

root.mainloop()
