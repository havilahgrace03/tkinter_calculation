import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("330x500")
root.resizable(False, False)
root.configure(bg="lightblue")
entry1=tk.Entry(root, font=("Arial", 16), bg="skyblue",fg="black", bd=2,justify="right")
entry1.grid(row=0, column=0, columnspan=4,padx=10, pady=12,ipady=10)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
r=1
c=0
def back():
    entry1.delete(len(entry1.get())-1, tk.END)
def clear():
    entry1.delete(0, tk.END)
def press(v):
    entry1.insert(tk.END, v)
def cal():
    try:
        res=eval(entry1.get())
        entry1.delete(0, tk.END)
        entry1.insert(0,res)
    except:
        entry1.delete(0, tk.END)
        entry1.insert(0,"Error")
for i in buttons:
    cmd= cal if i == '=' else lambda x=i: press(x)
    tk.Button(root,font=("bold", 18),bg="pink" if i in "+-*/=" else "lightgreen",fg="black",command=cmd,bd=1,text=
    i,width=5,height=2).grid(row=r,column=c,padx=2,pady=2,columnspan=1)
    c+=1
    if c==4:
        c=0
        r+=1

tk.Button(root,command=back,font=("bold",18),bg="black",fg="white",text="⌫",bd=2,width=5,height=2).grid(row=r,column=c+1,padx=2,pady=2,columnspan=1)
tk.Button(root,command=clear,font=("bold",18),bg="black",fg="white",text="C",bd=2,width=5,height=2).grid(row=r,column=c,padx=2,pady=2,columnspan=1)

root.mainloop()