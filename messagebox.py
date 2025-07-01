import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Message Box Application ")
root.minsize(300,200)

def show_info():
    messagebox.showinfo("Info", "This is an info message box.")
    
def show_warning():
    messagebox.showwarning("Warning", "This is a warning message box.")
    
def show_error():
    messagebox.showerror("Error", "This is an error message box.")
    
def show_question():
    messagebox.askquestion("Question", "Do you want to continue?")
    
    if answer == "yes":
        tk.Label(root, text="Good Morning").pack()
    else:
        tk.Label(root, text="Good Evening").pack()

btninfo = tk.Button(root, text="Click Info", command= show_info).pack()
btnwarning = tk.Button(root, text="Click Warning", command= show_warning).pack()
btnerror = tk.Button(root, text="Click Error", command= show_error).pack()
btnquestion = tk.Button(root, text="Click Question", command= show_question).pack()

root.mainloop()
