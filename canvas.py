import tkinter as tk

root = tk.Tk()
root.title("Drawing with Canvas")
root.minsize(300,200)

canvas = tk.Canvas(root, bg = "blue", height=500, width=500)

rect = 10,10, 100, 50
canvas.create_rectangle(rect, fill="green")

sqr = 10,10, 50, 50
canvas.create_rectangle(sqr, fill="red")

canvas.pack()

root.mainloop()