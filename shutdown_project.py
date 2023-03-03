from tkinter import *
import os
root=Tk()
root.title("Shutdown System")
root.geometry("400x580")
root.resizable(width=False,height=False)
def shutdown():
    os.system("shutdown /s /t 1")
def restart():
    os.system("shutdown /r /t 10")
def logout():
    os.system("shutdown -l")
#first button
shut=PhotoImage(file="power.png")
shutb=Button(root,image=shut,borderwidth=2,cursor="hand2",command=shutdown)
shutb.place(x=0,y=10)
#second button
res=PhotoImage(file="Restart.png")
resb=Button(root,image=res,borderwidth=2,cursor="hand2",command=restart)
resb.place(x=200,y=10)
#Third button
lout=PhotoImage(file="logout.png")
loutb=Button(root,image=lout,borderwidth=2,cursor="hand2",command=logout)
loutb.place(x=0,y=215)
#forth button
cl=PhotoImage(file="close.png")
clb=Button(root,image=cl,borderwidth=2,cursor="hand2",command=root.destroy)
clb.place(x=200,y=215)

l1=Label(root,text="Project Made By Ritesh Raj")
l1.place(x=130,y=550)
root.mainloop()
