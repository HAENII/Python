import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()

# Text
widget1 = tk.Text(root, width=10, height=10)
widget1.pack()
# ScrolledText
widget2 = ScrolledText(root, width=10, height=10)
widget2.pack()

root.mainloop()
