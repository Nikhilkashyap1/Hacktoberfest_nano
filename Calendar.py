from tkinter import *
import calendar

r=Tk()
r.title("Calendar")
r.geometry("270x240")
r.resizable(0,0)

def show():
	a=int(sb1.get())
	b=int(sb2.get())
	c=calendar.month(b,a)
	t.delete(0.0,END)
	t.insert(INSERT,c)
	
l1=Label(r,text="Month",font=('arial',9,'bold'))
l1.place(x=10,y=4)
l2=Label(r,text="Year",font=('arial',9,'bold'))
l2.place(x=160,y=4)

sb1=Spinbox(r,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
sb1.place(x=70,y=4)
sb2=Spinbox(r,from_=1999,to_=2100,width=4)
sb2.place(x=210,y=4)

b=Button(r,text="Show",font=('arial',9,'bold'),command=show).place(x=110,y=40)

t=Text(r,width=20,height=7)
t.place(x=50,y=90)

r.mainloop()