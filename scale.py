import tkinter as tk

root = tk.Tk()
root.title("The scale like thermometer")
root.minsize(300,200)

def scaleColor(value):
    if(int(value) <= 20):
        scale.config(bg="blue")
    elif(20 < int(value) <= 45):
        scale.config(bg="green")
    else:
        scale.config(bg="red")
        
    
    
scale = tk.Scale(root, length=250, from_=0, to=150, tickinterval=10,
                orient=tk.HORIZONTAL, label="Temperature", command=scaleColor)
scale.set(37)

scale.pack()

root.mainloop()
