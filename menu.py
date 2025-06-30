import tkinter as tk

root = tk.Tk()
root.title("Let's make a Menu")
root.minsize(300,200)

mainmenu = tk.Menu(root)

#File menu Started here

fileMenu = tk.Menu(mainmenu, tearoff= 0)

fileMenu.add_command(label="New Text File", command=lambda: print("New file created"))
fileMenu.add_command(label="New File")
fileMenu.add_command(label="New Window")
fileMenu.add_separator()
fileMenu.add_command(label="Open File")
fileMenu.add_command(label="Open Folder")

#open recent dropdown starts here
openrecent = tk.Menu(mainmenu)
openrecent.add_command(label="Open Recent File 1")
openrecent.add_command(label="Open Recent File 2")
openrecent.add_command(label="Open Recent File 3")
openrecent.add_command(label="Open Recent File 4")

fileMenu.add_cascade(label="Open Recent", menu=openrecent)

fileMenu.add_separator()

fileMenu.add_command(label="Exit", command=root.quit)

mainmenu.add_cascade(label="File", menu= fileMenu)

#Edit menu starts here
editMenu = tk.Menu(mainmenu, tearoff= 0)

editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")
editMenu.add_separator()
editMenu.add_command(label="Copy")
editMenu.add_command(label="Cut")
editMenu.add_command(label="Paste")
editMenu.add_separator()
editMenu.add_command(label="Find")
editMenu.add_command(label="Replace")

mainmenu.add_cascade(label="Edit", menu= editMenu)

root.config(menu=mainmenu)

root.mainloop()