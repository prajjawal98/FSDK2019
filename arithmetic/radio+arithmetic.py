from tkinter import*
obj=Tk()
obj.geometry("700x400+170+50")
obj.resizable(0,0)

l1=Label(text="first number")
l2=Label(text="second number")
e1=Entry(width=20)
e2=Entry(width=20)
e3=Entry(width=40)
e3.insert(0,"result is:")


def sum():
    if v.get==1:
        i=int(e1.get())
        j=int(e2.get())
        result=i+j
        total.set(result)
    elif v.get == 2:
        i = int(e1.get())
        j = int(e2.get())
        result = i - j
        total.set(result)
    elif v.get == 3:
        i = int(e1.get())
        j = int(e2.get())
        result = i * j
        total.set(result)
    elif v.get == 4:
        i = int(e1.get())
        j = int(e2.get())
        result = i ** j
        total.set(result)

def reset():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e3.insert(0, "result is")



v=IntVar()
total=IntVar()

l3=Label(text="select ur option",font=('arimo',10,'bold'))

r1=Radiobutton(text="SUM",variable=v,value=1,command=sum)
r2=Radiobutton(text="SUB",variable=v,value=2,command=sum)
r3=Radiobutton(text="MULTI",variable=v,value=3,command=sum)
r4=Radiobutton(text="POWER",variable=v,value=4,command=sum)

b1=Button(text="RESET",bd=3,command=reset,width=15)

l1.place(x=200,y=40)
e1.place(x=320,y=40)

l2.place(x=200,y=65)
e2.place(x=320,y=65)
l3.place(x=270,y=85)

r1.place(x=200,y=110)
r2.place(x=320,y=110)
r3.place(x=200,y=140)
r4.place(x=320,y=140)

b1.place(x=200,y=170)



e3.place(x=200,y=200)
obj.mainloop()
