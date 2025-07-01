import tkinter as tk

root = tk.Tk()
root.title("Text Widget")
root.minsize(300,200)

text = tk.Text(root)

text.insert("insert", "The first line in the text widget...\n")
text.insert("end", "The last line in the text widget...")

text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("next","2.0", "2.36")
text.tag_config("here", background="red")
text.tag_config("next", background="yellow")

root.mainloop()
