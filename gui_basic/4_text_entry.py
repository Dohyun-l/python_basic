from tkinter import *

root = Tk()
root.title("D582 GUI")
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5) # html의 textaear
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # Enter를 사용할 수 없음 # html의 input
e.pack()
e.insert(0, "한 줄만 입력해요")
# e.insert(END, "한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()