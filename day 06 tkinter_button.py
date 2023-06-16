import tkinter as tk
from tkinter.filedialog import askopenfilename

root = tk.Tk()

# 함수 생성
def open_file():
    filename = askopenfilename(filetypes=(("Excel files", ".xlsx .xls"), ('All files', '*.*')))
    if filename:
        print(filename)
        #btn_text.set("선택 완료")

#btn_text = tk.StringVar()
#btn_text.set("파일 선택") >>> textvariable = btn_text 로 선택에 따라 UI 가 변화하게 할 수 있음

# 버튼에 함수 연결
widget = tk.Button(
    root, 
    text = "파일 선택", 
    command=open_file,
    width=20,
    height=2,
    bg="blue",
    fg="yellow",
)
widget.pack()

root.mainloop()