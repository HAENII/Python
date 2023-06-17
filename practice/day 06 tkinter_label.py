import tkinter as tk
from PIL import ImageTk

root = tk.Tk()

# 텍스트 레이블
widget1 = tk.Label(
    root,
    text = "이것은 Label 입니다.",
    fg = "white",
    bg = "blue",
    width = 40,
    height = 5
)
widget1.pack()

# 이미지 레이블
img = ImageTk.PhotoImage(file="image.jpg")
widget2 = tk.Label(root, image = img)
widget2.pack()

root.mainloop()