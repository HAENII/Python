import tkinter as tk

root = tk.Tk()

# 위젯 생성
widget = tk.Listbox(root, width=50, height=10)
for i in range(1,50):
    widget.insert("end", f'{i}번')
scrollbar = tk.Scrollbar(root)

# 기능상호연결
widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=widget.yview)

# 배치
widget.pack(side="left", fill="y")
scrollbar.pack(side="right" , fill="y")

root.mainloop()