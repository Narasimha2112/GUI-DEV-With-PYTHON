import tkinter as tk

root = tk.Tk()
root.title("Radio Button Widget")
root.minsize(300,200)

tk.Label(root, text="Select Your Gender").pack()

for text, value in [("Male",1),("Female",2)]:
    tk.Radiobutton(root, text=text, value=value).pack()


root.mainloop()