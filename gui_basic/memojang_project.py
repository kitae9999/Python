import os
from tkinter import *
import tkinter.font 
root=Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")

filename="mynote.txt"

def open_file():
    if os.path.isfile(filename):  #절대경로를 사용하지 않고 파일명만 적어줄 경우 현재 파이썬을 실행한 디렉토리의 파일유무를 리턴
        txt.delete(1.0,END) #텍스트 위젯 본문 삭제
        with open("/Users/georgepark/PythonWorks/Pythonproject/gui_basic/mynote.txt","r",encoding="utf8") as op_file:
            lines=op_file.readlines() #모든 라인들을 가져와서 한줄씩 리스트형태로 저장
            for line in lines:
                txt.insert(1.0,line)
        

            
def save_file():
    saved_file=txt.get(1.0,END)
    with open("/Users/georgepark/PythonWorks/Pythonproject/gui_basic/mynote.txt","w",encoding="utf8") as sv_file:
        sv_file.write(saved_file)

menu=Menu(root)


menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label="열기",command=open_file)
menu_file.add_command(label="저장",command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기",command=root.quit)

menu.add_cascade(label="파일",menu=menu_file)

scrollbar=Scrollbar(root)
scrollbar.pack(side="right",fill="y")

txt=Text(root,width=640,height=480,yscrollcommand=scrollbar.set)
txt.pack()

txt.configure(font=("맑은 고딕",20,"roman"))


root.config(menu=menu)
root.mainloop()