from tkinter import *
from tkinter import messagebox
import tkinter.ttk

root = Tk()
root.title("윤대영어 문자 생성")
root.geometry("400x400")
root.resizable(1,1)
title = Label(root, text="안내문 작성")
title.pack()

notebook = tkinter.ttk.Notebook(root, width=300, height=300, takefocus=True)
notebook.pack(expand=True)

#How can I make notebook tab size to follow window size? 

frame1 = tkinter.ttk.Frame(notebook, width=400, height=280)
frame1.pack(expand=True)
notebook.add(frame1, text="1. 학생 정보 불러오기")

frame2 = Frame(root)
notebook.add(frame2, text="2. 진행 강좌 및 진도 안내")

frame3 = Frame(root)
notebook.add(frame3, text="3. TEST 안내")

frame4 = Frame(root)
notebook.add(frame4, text="4. 과제물 안내")

frame5 = Frame(root)
notebook.add(frame5, text="5. 안내사항")

frame6 = Frame(root)
notebook.add(frame6, text="6. 개인 안내사항")





root.mainloop()
