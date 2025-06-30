import tkinter as tk

root = tk.Tk()
root.title("Entry Widget")

label = tk.Label(root, text="Name:  ")
entry = tk.Entry(root)


label.pack()
entry.pack()


root.mainloop()