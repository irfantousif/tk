from tkinter import *
root=Tk()
k=Label(root,text="your good name sir:",)
K=Entry(root)
h=Label(root,text='your phone no:')
H=Entry(root)
a=Label(root,text='customer pin:')
A=Entry(root)
l=Label(root,text='price:')
L=Entry(root)
i=Label(root,text='gender:')
I=Entry(root)
d=Label(root,text='age:')
D=Entry(root)
k.grid(row=0,sticky=E)
h.grid(row=1,sticky=E)
a.grid(row=2,sticky=E)
l.grid(row=3,sticky=E)
i.grid(row=4,sticky=E)
d.grid(row=5,sticky=E)
K.grid(row=0,column=1)
H.grid(row=1,column=1)
A.grid(row=2,column=1)
L.grid(row=3,column=1)
I.grid(row=4,column=1)
D.grid(row=5,column=1)
c=Checkbutton(root,text="HOPE TOU LIKED OUR HARD WORK")
c.grid(columnspan=2)
root.mainloop()
