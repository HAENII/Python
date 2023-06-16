import tkinter as tk

root = tk.Tk()

# 텍스트 
widget1 = tk.Text(root, width=50,height=10)
widget1.pack()

# 버튼 (command lambda 함수 작성)
widget2 = tk.Button(root, text="삭제하기" , command=lambda : widget1.delete(1.0 , "end"))
widget2.pack()

root.mainloop()