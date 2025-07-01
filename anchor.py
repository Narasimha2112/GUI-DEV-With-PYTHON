import tkinter as tk

root = tk.Tk()
root.title("Anchors & Widget")
root.minsize(300,200)

frame = tk.Frame(root).pack()
tk.Label(frame, text="North").pack(anchor="e")

root.mainloop()
