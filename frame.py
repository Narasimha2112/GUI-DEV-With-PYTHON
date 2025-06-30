import tkinter as tk

root = tk.Tk()
root.title("Widget in Window with Frame")
root.minsize(300,200)

frame = tk.Frame(root,bg="red", height= 400, width=400)

tk.Label(frame, text="Hello I'm Jack Sparrow").pack()

frame.pack()

root.mainloop()