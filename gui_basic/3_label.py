from tkinter import *

root=Tk()
root.title("Nado GUI")
root.geometry("640x480")
label1=Label(root,text="안녕하세요")
label1.pack()

def change():
    label1.config(text="또 만나요")
    
btn=Button(root,text="클릭",command=change)
btn.pack()

root.mainloop()