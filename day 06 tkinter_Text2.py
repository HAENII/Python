import tkinter as tk

root = tk.Tk()

# 1.0 맨 위
widget1 = tk.Text(root, width=50,height=10)
widget1.insert(1.0, "1st placeholder. write your name\n")
widget1.insert(1.0, "2nd placeholder. write your age.\n")
widget1.insert(1.0, "3rd placeholder. write your job.\n") 
widget1.pack()

# end 맨 밑
widget2 = tk.Text(root, width=50,height=10)
widget2.insert("end", "1st placeholder. write your name\n")
widget2.insert("end", "2nd placeholder. write your age.\n")
widget2.insert("end", "3rd placeholder. write your job.\n") 
widget2.pack()

#x.y: x번쨰 줄, y번째 글자
widget3 = tk.Text(root, width=50,height=10)
widget3.insert("end", "---------------------------\n")
widget3.insert("end", "---------------------------\n")
widget3.insert("end", "---------------------------\n") 
widget3.insert(2.7, "0")
widget3.pack()

root.mainloop()