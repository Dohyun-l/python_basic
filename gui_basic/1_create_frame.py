from tkinter import *

root = Tk()
root.title("D582 GUI")
root.geometry("640x480") # 가로 * 세로
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False) # x(너비), y(너비) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()