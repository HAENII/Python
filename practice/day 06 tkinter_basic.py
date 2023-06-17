import tkinter as tk

root = tk.Tk()
# 정확하게 좌표로 지정하려면 .place(x,y)
# 그리드로 나눠 행과 열 번호를 지정하는 .grid()
# 순서대로 하나씩 추가함 .pack()

# Label 1
widget1 = tk.Label(
    root , 
    text = "This is a label" , 
    fg = "white" , 
    bg = "#34A2FE" , 
    width = 40 ,
    height = 5)

widget1.pack() 

# Button
widget2 = tk.Button(root , text = "This is a button")
widget2.pack

# Text
widget3 = tk.Text(root, width=10, height=10)
widget3.pack()

# scrolled Text
#widget4 = tk.ScrolledText(root, width=10 , height=10)
#widget4.pack()

# Listbox
widget5 = tk.Listbox(root)
widget5.pack()

root.mainloop()
