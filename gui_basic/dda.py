note_file=open("/Users/georgepark/PythonWorks/Pythonproject/gui_basic/mynote.txt","r",encoding="utf8")
lines=note_file.readlines() #모든 라인들을 가져와서 한줄씩 리스트형태로 저장
note_file.close()

write_file=open("/Users/georgepark/PythonWorks/Pythonproject/gui_basic/mynote.txt","a",encoding="utf8")
for line in lines:
    write_file.write(line)

write_file.close()