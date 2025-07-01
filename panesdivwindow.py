import tkinter as tk

root = tk.Tk()
root.title("Dividing with Panes")
root.minsize(300,200)

panedwindow = tk.PanedWindow(root, bg="pink", orient="vertical")

panedwindow.pack()

l1 = tk.Label(panedwindow, text="Pane1")
panedwindow.add(l1)
l2 = tk.Label(panedwindow, text="Pane2")
panedwindow.add(l2)
l3 = tk.Label(panedwindow, text="Pane3")
panedwindow.add(l3)



root.mainloop()
