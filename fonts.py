import tkinter as tk
from tkinter.font import Font
root = tk.Tk()
root.title("Attention with Fonts")
root.minsize(300,200)

font1 = Font(
    family='Arial',
    size=20,
    weight='bold',
    slant='italic',
    underline=1,
    overstrike=1
)
tk.Label(root, text="hello ", font=font1).pack()

root.mainloop()
