import tkinter as tk

window = tk.Tk()

e = tk.Entry(window,show='*')
e.pack()

t = tk.Text(window,height=2)
t.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert('end',var)

b1 = tk.Button(window,text="insert point",width=15,height=2,command=insert_point)
b1.pack()

b2 = tk.Button(window,text="insert end",command=insert_end)
b2.pack()

# list
def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

var1 = tk.StringVar()
l1 = tk.Label(window,textvariable=var1,bg="yellow")
l1.pack()

b3 = tk.Button(window, text='print selection', command=print_selection)
b3.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44)) 
lb = tk.Listbox(window, listvariable=var2)  
lb.pack()

window.mainloop()

