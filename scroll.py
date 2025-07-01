import tkinter as tk

root = tk.Tk()
root.title("Displaying a list of items")
root.minsize(300,200)

l = tk.Listbox(root, justify="center", selectbackground="green")

scroll = tk.Scrollbar(root, command=l.yview)

l.config(yscrollcommand=scroll.set)

scroll.pack(side="right", fill="y")

for item in range(100):
    l.insert("end",item)
    
l.pack()

root.mainloop()