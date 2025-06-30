import tkinter as tk

root = tk.Tk()
root.title("Check Button Widget")
root.minsize(300,200)

tk.Label(root, text="Select your Languages").pack()

tk.Checkbutton(root, text="Tkinter").pack()
tk.Checkbutton(root, text="Django").pack()
tk.Checkbutton(root, text="Flask").pack()


root.mainloop()