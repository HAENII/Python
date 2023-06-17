from tkinter import *
from tkinter.filedialog import *
import os

def newfile() : 
    root.title("새로운 나만의 일기장")
    ta.delete(1.0 , END)

def openfile() :
    file = askopenfilename(initialdir = "/" ,  title = "파일 선택" , filetypes=(("text files", "*.txt"), ("all file" , "*.*")))
    root.title(os.path.basename(file) + "- 메모장")
    ta.delete(1.0 , END)
    f = open(file , "r")
    ta.insert(1.0 , f.read())
    f.close

def savefile():
    f = asksaveasfile(mode = "w" , defaultextension= ".txt")
    if f is None :
        return
    ts = str(ta.get(1.0 , END))
    f.write(ts)
    f.close

root = Tk()

root.title("나만의 일기장")
root.geometry("400x400")

widget1 = Label(
    root,
    text = "오늘의 일기",
    bg="white",
    fg="tomato"
)
widget1.pack()

ta = Text(root)
sb = Scrollbar(ta)
sb.config(command = ta.yview)
root.grid_rowconfigure(0 , weight=1)
root.grid_columnconfigure(0 , weight=1)
sb.pack(side = RIGHT , fill = Y)

mb = Menu(root)
fi = Menu(mb , tearoff=0)
fi.add_command(label = "새파일" , command  = newfile)
fi.add_command(label = "열기" , command=openfile)
fi.add_command(label = "저장" , command=savefile)
fi.add_separator()
fi.add_command(label = "종료" , command= root.destroy)
mb.add_cascade(label = "파일" , menu = fi )

root.config(menu = mb)

widget2 = Text(
    root,
    fg="blue",
    width=40,
    height=40
)
widget2.pack()

widget3 = Label(
    root, 
    text = "이것은 라벨입니다.",
    bg = "beige",
    fg = "black"
)
widget3.pack()
root.mainloop()
