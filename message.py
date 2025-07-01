import tkinter as tk

root = tk.Tk()
root.title("Multiple lines with Message")
root.minsize(300,200)

tk.Message(root, text="we can say that tkinter is", bg="red").pack()


root.mainloop()
