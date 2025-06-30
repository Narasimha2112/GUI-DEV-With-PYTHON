import tkinter as tk

root = tk.Tk()
root.title("Displaying a list of items")
root.minsize(300,200)

l = tk.Listbox(root, justify="center", selectbackground="green")

for item in range(10):
    l.insert("end",item)
    
l.pack()

root.mainloop()