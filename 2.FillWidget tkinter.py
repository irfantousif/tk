from tkinter import *
root=Tk()
l1=Label(root,text="one",fg='blue',bg='black')
l1.pack()
l2=Label(root,text="two",fg='red',bg='blue')
l2.pack(fill=X)
l3=Label(root,text="three",fg='blue',bg='red')
l3.pack(side=LEFT,fill=Y)
root.mainloop()
#ading to the window by using pack