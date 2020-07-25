from tkinter import *
root=Tk()
topf=Frame(root)
topf.pack()
bottomf=Frame(root)
bottomf.pack(side=BOTTOM)
b1=Button(topf,text='Login',fg='violet')
b1.pack(side=LEFT)
b2=Button(topf,text='Clear',fg='pink')
b2.pack(side=LEFT)
b3=Button(bottomf,text='Exit',fg='red')
b3.pack(side=BOTTOM)
root.mainloop()

