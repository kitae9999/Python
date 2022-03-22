from tkinter import *

root=Tk()
root.title("Nado GUI")
btn1=Button(root,text="버튼1")
btn1.pack()

btn2=Button(root,padx=5,pady=10,text="버튼2")
btn2.pack()

btn3=Button(root,padx=10,pady=5,text="버튼3")
btn3.pack()

btn4=Button(root,width=10,height=3,text="버튼4")
btn4.pack()

btn5=Button(root,fg="red",bg="yellow",text="버튼5")
btn5.pack()

def btncmd():
    print("버튼이 클릭되었습니다")

btn6=Button(root,text="동작하는 버튼",command=btncmd)
btn6.pack()
root.mainloop()