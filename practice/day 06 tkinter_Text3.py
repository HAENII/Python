import tkinter as tk

root = tk.Tk()

widget = tk.Text(root, width=50, height=10)

widget.config(state="normal")
widget.insert(1.0 , "삭제할 수 없는 텍스트입니다.")
widget.config(state="disabled")

widget.pack()

root.mainloop()