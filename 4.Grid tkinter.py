from tkinter import *
root=Tk()
ul=Label(root,text='User Name:')
pl=Label(root,text='Password:')
ue=Entry(root)
pe=Entry(root)

ul.grid(row=0,sticky=E)
pl.grid(row=1,sticky=E)
ue.grid(row=0,column=1)
pe.grid(row=1,column=1)
c=Checkbutton(root,text="Remember Me")
c.grid(columnspan=2)
lb=BitmapImage
root.mainloop()
