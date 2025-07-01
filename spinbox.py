import tkinter as tk

root = tk.Tk()
root.title("SpinBOx")
root.minsize(300,200)

tk.Spinbox(root, from_=0, to=100).pack()

root.mainloop()
