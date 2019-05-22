from tkinter import*
obj=Tk()
obj.title("calculator")
obj.geometry("160x280+100+50")



textin=StringVar()
operator=""

def clickbut(number):
    global operator
    operator=operator+str(number)
    textin.set(operator)

def equalbut():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator=''

def equalbut():
    global operator
    sub=str(eval(operator))
    textin.set(sub)
    operator=''

def equalbut():
    global operator
    mul=str(eval(operator))
    textin.set(mul)
    operator=''

def equalbut():
    global operator
    div=str(eval(operator))
    textin.set(div)
    operator=''

def clrbut():
    textin.set('')


objtext=Entry(obj,font=("courier New",15,'bold'),textvar=textin,width=25,bd=5,bg='powder blue')
objtext.pack()


b1=Button(obj,text="c",width=10,command=clrbut,bg="cyan")
b2=Button(obj,text="/",width=4,command=lambda:clickbut("/"))

b5=Button(obj,text="7",width=4,command=lambda:clickbut(7))
b6=Button(obj,text="8",width=4,command=lambda:clickbut(8))
b7=Button(obj,text="9",width=4,command=lambda:clickbut(9))
b8=Button(obj,text="-",width=4,command=lambda:clickbut("-"))
b9=Button(obj,text="4",width=4,command=lambda:clickbut(4))
b10=Button(obj,text="5",width=4,command=lambda:clickbut(5))
b11=Button(obj,text="6",width=4,command=lambda:clickbut(6))
b12=Button(obj,text="+",width=4,command=lambda:clickbut("+"))
b13=Button(obj,text="1",width=4,command=lambda:clickbut(1))
b14=Button(obj,text="2",width=4,command=lambda:clickbut(2))
b15=Button(obj,text="3",width=4,command=lambda:clickbut(3))
b16=Button(obj,text="=",width=4,height=3,bg="cyan",command=equalbut)

b17=Button(obj,text="0",width=9,command=lambda:clickbut(0))
b18=Button(obj,text=".",width=4,command=lambda:clickbut("."))


b1.place(x=0,y=130,)
b2.place(x=120,y=130)

b5.place(x=0,y=160)
b6.place(x=40,y=160)
b7.place(x=80,y=160)
b8.place(x=120,y=160)
b9.place(x=0,y=190)
b10.place(x=40,y=190)
b11.place(x=80,y=190)
b12.place(x=120,y=190)
b13.place(x=0,y=220)
b14.place(x=40,y=220)
b15.place(x=80,y=220)
b16.place(x=120,y=220)

b17.place(x=0,y=250)
b18.place(x=80,y=250)


obj.mainloop()