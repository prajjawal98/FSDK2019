from tkinter import*
obj=Tk()
obj.geometry("700x400+170+50")
obj.resizable(0,0)

l1=Label(text="enter the first number")
l2=Label(text="enter the second number")
e1=Entry(width=20)
e2=Entry(width=20)
e3=Entry(width=40)
e3.insert(0,"result is:")

def sum():
    i=e1.get()
    j=e2.get()
    result=int(i)+int(j)
    e3.delete(0,END)
    e3.insert(0,"sum is{}".format(result))

def sub():
    i = e1.get()
    j = e2.get()
    result = int(i) - int(j)
    e3.delete(0, END)
    e3.insert(0, "sub is{}".format(result))

def multi():
    i = e1.get()
    j = e2.get()
    result = int(i) * int(j)
    e3.delete(0, END)
    e3.insert(0, "multi is{}".format(result))

def power():
    i = e1.get()
    j = e2.get()
    result = int(i)**int(j)
    e3.delete(0, END)
    e3.insert(0, "power is{}".format(result))


def reset():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e3.insert(0,"result is")

b1=Button(text="SUM",bd=3,command=sum,width=15)
b2=Button(text="RESET",bd=3,command=reset,width=15)
b3=Button(text="SUB",bd=3,command=sub,width=15)
b4=Button(text="MULTI",bd=3,command=multi,width=15)
b5=Button(text="POWER",bd=3,command=power,width=15)

l1.place(x=200,y=40)
e1.place(x=320,y=40)

l2.place(x=200,y=65)
e2.place(x=320,y=65)

b1.place(x=200,y=90)
b2.place(x=320,y=90)
b3.place(x=200,y=120)
b4.place(x=320,y=120)
b5.place(x=250,y=160)

e3.place(x=200,y=200)
obj.mainloop()
